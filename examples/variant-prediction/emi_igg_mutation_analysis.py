# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 21:20:42 2022

@author: makow
"""

import pandas as pd
import numpy as np
import scipy as sc
from scipy import spatial

data = pd.read_csv("C:\\Users\\makow\\Documents\\GitHub\\esm\\examples\\variant-prediction\\igg_binding.csv", header = 0, index_col = 0)
wt = list('QVQLVQSGAEVKKPGASVKVSCKASGYTFTDYYMHWVRQAPGQGLEWMGRVNPNGRGTTYNQKFEGRVTMTTDTSTSTAYMELRSLRSDDTAVYYCARSNLLDDWGQGTTVTVSS')

mutation = []
for i in data.index:
    mut = list(i)
    if sc.spatial.distance.hamming(mut, wt)*115 == 1:
        for j in np.arange(115):
            wt_res = wt[j]
            mut_res = mut[j]
            if wt_res != mut_res:
                mutation.append([''.join([wt_res, str(j), mut_res]), data.loc[i,'ANT Binding'], data.loc[i,'OVA Binding']])

alph_sorted = list('ACDEFGHIKLMNPQRSTVWY')
mutation = []
for i in np.arange(115):
    wt_res = wt[i]
    for ii in alph_sorted:
        mutation.append([''.join([wt_res, str(i), str(ii)])])
            
    
mutation = pd.DataFrame(mutation)
mutation.to_csv('emi_igg.csv', header = True, index = True)



