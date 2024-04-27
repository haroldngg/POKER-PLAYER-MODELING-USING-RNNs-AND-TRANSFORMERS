# Sequential models for Poker player modelisation

There is two type of models available :
  - The RRN+Transformer structure
  - The Full Transformer version

## RRN+Transformer
file : RNN+Transformer/modelisation_joueur_RNN+transformer.ipynb

To be frank, It won't be crazy.


## Transformer
file : Transformer/modelisation_joueur_transformer.ipynb

View already existing learning graphs in Transformer/model_cv_300epochs

### Choosing the right dataset
basic_dataset : data_transformer
duplicated data_set : dataset_transformer_duplicated

Remarks : The dataset_transformer_duplicated file is compressed in the format .tar.xz (.zip was too heavy)

to change dataset, change the file name in the cell under "Datasets : cell" line 1 : 
with open("./name_of_the_dataset", "rb") as temp:


How to select the differents hyperparameters :

### Models hyperparameter : 
See "Parametre variables" cell.

dim_embedding = ...
layer_size_embedding = ...
...


### Training hyperparameters :
see line :  acc_list, loss_list = trainer(training_data, test_data, modelisation_joueur, loss_fn = nn.CrossEntropyLoss(), epoch=50, batchsize=256*24, rate=1e-4)

epoch, batchsize, rate are in the inputs of the function trainer()



