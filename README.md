# RezoJDM16k (French Knowledge Graph DataSet)
This repository introduces RezoJDM16K a French Knowledge Graph Dataset with 53 semantic relations created from RezoJDM. Different graph embeddings have gained from this dataset which are available for semantic link prediction task.

## Instruction:  

Simply download the `./benchmarks/RezoJDM16K` folder and use it for Knowledge Graph Emebedding Models available in OpenKE. Run jupyter notebook `./src/4-OpenKE_2_KGE_Models.ipynb` which is created for this purpose.  

## Description of Source Notebooks

The source jupyter notebooks in this repository is for recreation the dataset with RezoJDM dump: 
- 1-Dump2CSVs.ipynb : converts RezoJDM dumps to CSV format files with simple preliminary filters.
- 2-CSV2Triplets.ipynb : converts CSV format files into triplets.
- 3-Triplets2OpenKE.ipynb : convert triplets to OpenKE graph format.
- 4-OpenKE_2_KGE_Models.ipynb : use OpenKE graphs for trainnig with different knowledge graph embedding models.  


## Performance:  

Here are the performance of different Knowledge Graph Embeddings Models run on RezoJDM16K compared to other English datasets.  


|Model			|	RezoJDM16k  |	WN18RR	|	FB15k237	| WN18RR (Paper\*)| FB15k237  (Paper\*)|
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
  booktitle={forthcoming},
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

