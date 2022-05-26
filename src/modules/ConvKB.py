import torch
import torch.nn as nn
import torch.nn.functional as F
from .Model import Model

class ConvKB(Model):

    def __init__(self, ent_tot, rel_tot, convkb_drop_prob, out_channels, kernel_size, hidden_size = 100):
        super(ConvKB, self).__init__(ent_tot, rel_tot)
        
        self.hidden_size = hidden_size
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.convkb_drop_prob = convkb_drop_prob


        self.ent_embeddings = nn.Embedding(self.ent_tot, self.hidden_size)
        self.rel_embeddings = nn.Embedding(self.rel_tot, self.hidden_size)

        self.conv1_bn = nn.BatchNorm2d(1)
        self.conv_layer = nn.Conv2d(1, self.out_channels, (self.kernel_size, 3))  # kernel size x 3
        self.conv2_bn = nn.BatchNorm2d(self.out_channels)
        self.dropout = nn.Dropout(self.convkb_drop_prob)
        self.non_linearity = nn.ReLU() # you should also tune with torch.tanh() or torch.nn.Tanh()
        self.fc_layer = nn.Linear((self.hidden_size - self.kernel_size + 1) * self.out_channels, 1, bias=False)

        self.criterion = nn.Softplus()

        nn.init.xavier_uniform_(self.ent_embeddings.weight.data)
        nn.init.xavier_uniform_(self.rel_embeddings.weight.data)		

        nn.init.xavier_uniform_(self.fc_layer.weight.data)
        nn.init.xavier_uniform_(self.conv_layer.weight.data)


    def _calc(self, h, t, r):
        h = h.unsqueeze(1) # bs x 1 x dim
        r = r.unsqueeze(1)
        t = t.unsqueeze(1)

        conv_input = torch.cat([h, r, t], 1)  # bs x 3 x dim
        conv_input = conv_input.transpose(1, 2)
        # To make tensor of size 4, where second dim is for input channels
        conv_input = conv_input.unsqueeze(1)
        conv_input = self.conv1_bn(conv_input)
        out_conv = self.conv_layer(conv_input)
        out_conv = self.conv2_bn(out_conv)
        out_conv = self.non_linearity(out_conv)
        out_conv = out_conv.view(-1, (self.config.hidden_size - self.config.kernel_size + 1) * self.config.out_channels)
        input_fc = self.dropout(out_conv)
        score = self.fc_layer(input_fc).view(-1)

        return -score

    def loss(self, score, regul):
        return torch.mean(self.criterion(score * self.batch_y)) + self.config.lmbda * regul


    def forward(self, data):
        batch_h = data['batch_h']
        batch_t = data['batch_t']
        batch_r = data['batch_r']

        h = self.ent_embeddings(batch_h)
        t = self.ent_embeddings(batch_t)
        r = self.rel_embeddings(batch_r)

        score = self._calc(h, r, t)

        # regularization
        l2_reg = torch.mean(h ** 2) + torch.mean(t ** 2) + torch.mean(r ** 2)
        for W in self.conv_layer.parameters():
            l2_reg = l2_reg + W.norm(2)
        for W in self.fc_layer.parameters():
            l2_reg = l2_reg + W.norm(2)

        return self.loss(score, l2_reg)


    def predict(self, data):
        
        score = self.forward(data)

        return score.cpu().data.numpy()