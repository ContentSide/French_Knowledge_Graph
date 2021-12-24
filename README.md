# RezoJDM-SDS (Semantic DataSet)
This is a subproject related to the creation of RezoJDM-SDS, French Semantic Relation DataSet with 10 semantic types. RezoJDM-SDS is extracted under several constraints from RezoJDM a French lexical-semantic network.

## Instruction:  

Simply download the `datasets` folder and use it for training machine learning models. There are two main columns in the datasets, namely, `source_name`,`destination_name` and the rest of columns are semantic relations: `r_agent`, `r_carac`, `r_causatif`, `r_conseq`, `r_has_part`, `r_holo`, `r_instr`, `r_isa`, `r_lieu`, `r_patient`.  

## Instruction:  

Here are the performance of different Knowledge Graph Embeddings Models run on RezoJDM16K compared to other English datasets.  


|Model			|	RezoJDM16K  |	WN18RR	|	FB15K237	| WN18RR (Paper\*)| FB15K237  (Paper\*)|
|:-:		|:-:	|:-:  |:-:  |:-:  |:-:  |
|TransE	|0.512	|0.512	|0.476|0.501|0.486|
|TransH	|0.512	|0.507	|0.490|-|-|
|TransR	|0.512	|0.519	|0.511|-|-|
|TransD	|0.512	|0.508	|0.487|-|-|
|DistMult	|0.512	|0.479	|0.419|0.49|0.419|
|ComplEx	|0.512	|0.485	|0.426|0.51|0.428|
|ConvE		|0.512	|0.506	|0.485|0.52|0.501|
|RotatE	|0.512	|0.549	|0.479|-|0.480|
|RotatE (+adv)	|0.583	|0.565	|0.522|0.571|0.533|


## RezoJDM-SDS: Description

RezoJDM-SDS is a Semantic DataSet created from RezoJDM. Among wide variety of possibilities, we have only focused on 10 most frequent semantic relations which belong to the ontological and predicative categories of RezoJDM and are more common in semantic linguistic analysis.  Relations with weights less than 50 are treated as negative in our dataset. 

<p align="center">
  <img src="./resources/pics/Table_1.jpg" width="500" height="300">
</p>

We have selected reliable relations with weights greater than 50 in RezoJDM. This constraint guarantees to select positive relations that have been validated more frequently by different players in the JDM game. 

<p align="center">
  <img src="./resources/pics/Table_1.jpg" width="500" height="350">
</p>

The descriptions and examples of the relation types are illustrated in tables. RezoJDM-SDS is gained by randomly splitting the initial dataset into two train and test samples (80\% and 20\%).  

<p align="center">
  <img src="./resources/pics/Table_1.jpg" width="500" height="150">
</p>

## Citations
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
RezoJDM-SDS is released under the MIT license.

