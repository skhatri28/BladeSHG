# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:09:22 2017

@author: sanjaykhatri
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
allFiles = glob.glob("*.txt") # includes all files into a single stucture 
frame = pd.DataFrame()
df = pd.DataFrame()

for i,file_ in enumerate(allFiles):
#    f = open(file_,'r')
#     for j,line in enumerate(f):
#         if j == 1:
#             date = line[14:22]
#             break
    df = pd.read_csv(file_,index_col = None, header=None, skiprows = 10, skipfooter = 1, delimiter = '\t')
    print(df)