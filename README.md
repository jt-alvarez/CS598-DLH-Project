# Deep Learning for Healthcare - Final Project

This repository provides the code for running PreTrained ClinicalBERT model and 3 PyHealth package based Transformer with MultiHeaded Attention models.

# Notebook to Run the Code:
  
DL4H_Team_152_combine.ipynb 


## Dependencies

  - python=3.12
  - NumPy
  - PyTorch
  - scikit-learn
  - conda-forge::transformers
  - conda-forge::dataset
  - tqdm=4.62.2
  - pandas
  - packaging
  - accelerate
  - conda-forge::jupyterlab
  - conda-forge::notebook
  - conda-forge::ipywidgets
  - scispacy
  - en_core_sci_sm

## Installation
 
Use pip to install, typical install time is about 30 minutes.

* the en_core_sci_sm for scispacy has a special install using this command
* pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz 

## How to load sample data

An example to sample data is located at Notebook code execution section.

* In order to Run Approach 2 - PyHealth Implementation, Dataset need to be downloaded in "./mimic-iv-2.2/hosp".

* In order to run Approach 2 - PreTrained Model, the Mimic-IV dataset must be access from https://physionet.org/content/mimiciv/ which requires ethics training and privacy concerns. 





