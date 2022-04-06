# RezoJDM16k (French Knowledge Graph DataSet)
This repository introduces RezoJDM16K a French Knowledge Graph Dataset with 53 semantic relations created from RezoJDM. Different graph embeddings have been gained from this dataset which are available for semantic link prediction tasks.

## Instruction:  

Simply, download the `./benchmarks/RezoJDM16K` folder and use it for Knowledge Graph Embedding Models available in OpenKE. Run Jupiter notebook `./src/4-OpenKE_2_KGE_Models.ipynb` which is created for this purpose.
  

## Description of Source Notebooks

The Jupiter notebooks in `./src` are for recreation the dataset with RezoJDM dump: 
- 1-Dump2CSVs.ipynb : converts RezoJDM dumps to CSV format files with simple preliminary filters.
- 2-CSV2Triplets.ipynb : converts CSV format files into triplets.
- 3-Triplets2OpenKE.ipynb : convert triplets to OpenKE graph format.
- 4-OpenKE_2_KGE_Models.ipynb : use OpenKE graphs for trainnig with different knowledge graph embedding models.  


## Performance:  

Here is the performance of knowledge graph embedding models for RezoJDM16k considering the different evaluation metrics \[[1](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9220143)\]  

Model			|	MRR  |	MR	|	Hit@10	| Hit@3| Hit@1|
|:-:		|:-:	|:-:  |:-:  |:-:  |:-:  |
|TransE	|0.179	|203.31	|0.432|0.242|0.041|
|TransH	|0.218	|177.12	|0.498|0.291|0.069|
|TransD	|0.216	|170.68	|0.500|0.287|0.066|
|DistMult	|0.220	|194.47	|0.445|0.252|0.109|
|ComplEx	|0.253	|201.58	|0.533|0.304|0.117|




Here is the performance ((Hit@10)) of the different Knowledge Graph Embeddings Models run on RezoJDM16K compared to other English datasets. 


|Model			|	RezoJDM16k  |	WN18RR	|	FB15k237	| WN18RR \[[2](https://aclanthology.org/D15-1174.pdf)\]| FB15k237  \[[2](https://aclanthology.org/D15-1174.pdf)\]|
|:-:		|:-:	|:-:  |:-:  |:-:  |:-:  |
|TransE	|0.422	|0.512	|0.476|0.501|0.486|
|TransH	|0.474	|0.507	|0.490|-|-|
|TransD	|0.470	|0.508	|0.487|-|-|
|DistMult	|0.424	|0.479	|0.419|0.49|0.419|
|ComplEx	|0.528	|0.485	|0.426|0.51|0.428|
|RotatE (+adv)	|0.583	|0.565	|0.522|0.571|0.533|


## RezoJDM16K Dataset Citation
```bibtex
@inproceedings{mirzapour2022,
  title={Introducing RezoJDM Knowledge Graph DataSet for Link Prediction},
  author={Mehdi Mirzapour, Waleed Ragheb, Mohammad Javad Saeedizade,Kevin Cousot, Helene Jacquenet, Lawrence Carbon, Mathieu Lafourcade},
  booktitle={({{To}} Appear) Proceedings of the 13th Language Resources and Evaluation Conference (LREC)},
  year={2022}
}
```


## RezoJDM Citations
```bibtex
@inproceedings{lafourcade2007making,
  title={Making people play for Lexical Acquisition with the JeuxDeMots prototype},
  author={Lafourcade, Mathieu},
  booktitle={SNLP'07: 7th international symposium on natural language processing},
  pages={7},
  year={2007}
}
```

### License
`RezoJDM16K` is released under the MIT license.

