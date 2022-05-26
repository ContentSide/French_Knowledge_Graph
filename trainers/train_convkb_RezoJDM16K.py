import openke
from openke.config import Trainer, Tester
from openke.module.model import ConvKB
from openke.module.loss import SigmoidLoss
from openke.module.strategy import NegativeSampling
from openke.data import TrainDataLoader, TestDataLoader

# dataloader for training
train_dataloader = TrainDataLoader(
	in_path = "./benchmarks/RezoJDM16K/", 
	batch_size = 2000,
	threads = 8,
	sampling_mode = "cross", 
	bern_flag = 0, 
	filter_flag = 1, 
	neg_ent = 64,
	neg_rel = 0
)

# dataloader for test
test_dataloader = TestDataLoader("./benchmarks/RezoJDM16K/", "link")

# define the model
convkb = ConvKB(
	ent_tot = train_dataloader.get_ent_tot(),
	rel_tot = train_dataloader.get_rel_tot(),
    convkb_drop_prob = 0.3,
    out_channels = 64,
    kernel_size = 1,
    hidden_size = 100
)

# define the loss function
model = NegativeSampling(
	model = convkb, 
	loss = SigmoidLoss(adv_temperature = 2),
	batch_size = train_dataloader.get_batch_size(), 
	regul_rate = 0.0
)

# train the model
trainer = Trainer(model = model, data_loader = train_dataloader, train_times = 50, alpha = 2e-5, use_gpu = True, opt_method = "adam")
trainer.run()
convkb.save_checkpoint('./checkpoint/rotate.ckpt')

# test the model
convkb.load_checkpoint('./checkpoint/rotate.ckpt')
tester = Tester(model = convkb, data_loader = test_dataloader, use_gpu = True)
tester.run_link_prediction(type_constrain = False)