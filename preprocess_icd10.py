import logging
import os
from typing import Callable, Dict, List, Optional, Tuple
import csv
import json, time
from collections import defaultdict
from datetime import datetime
from itertools import combinations, islice
import pickle

import pandas as pd

import torch
torch.__version__

#data_df = pd.read_csv('/data/corpora_alpha/MIMIC/physionet.org/files/mimiciv/2.2/hosp/admissions.csv.gz', nrows=None, compression='gzip', 
#            dtype={'subject_id': str, 'hadm_id': str},
#            on_bad_lines='skip')



'''
data_df = pd.read_csv('/data/corpora_alpha/MIMIC/physionet.org/files/mimiciv/2.2/hosp/diagnoses_icd.csv.gz', nrows=None, compression='gzip',
            dtype={'subject_id': str, 'hadm_id': str, 'icd_code': str, 'icd_version': str},
            on_bad_lines='skip')
'''

data_df = pd.read_csv('./mimic-iv-2.2/hosp/diagnoses_icd.csv.gz', nrows=None, compression='gzip',
            dtype={'subject_id': str, 'hadm_id': str, 'icd_code': str, 'icd_version': str},
            on_bad_lines='skip')


data_df_icd_10 = data_df[data_df['icd_version'] == "10"]

#print(data_df_icd_10)
#print(len(data_df_icd_10))

#dir_path = './mimic3/autoicd_pretrain/data_example/diagnosis_icd10.csv'
dir_path = './mimic-iv-2.2/hosp/diagnosis_icd10.csv'

data_df_icd_10.to_csv(dir_path, index=False)
#f1 = open(dir_apth + '/diagnosis_icd10.csv', 'w')

#for ind, row in data_df.iterrows():
#    if row['icd_version'] == "10":
#        f1.write("{0}{1}\n".format(ind,row))


#f1.close()

print("Done")




