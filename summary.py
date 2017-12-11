# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:01:55 2017

@author: laksh
"""

import pandas as pd
#%%
df =pd.read_csv('CleanedData.csv',index_col=0)

def maxval(l):
    mymax = 0
    for data in l:
        if data >= mymax:
            mymax = data
    return mymax

num = maxval (df['Hospice Beneficiaries'])
print('Greatest number of hospice beneficiaries',num )
#%%
#MEAN, MEDIAN AND STANDARAD DEVIATION OF AVerage age and Total Medicare Payment 
#Total summary statistics
mean_age=df['Average Age'].mean()
print('Mean age of people under hospice care',mean_age)
#%%
mean_payment=df['Total Medicare Payment Amount'].mean()
print('Mean of Total Medicare Payment Amount',mean_payment)

std_payment=df['Total Medicare Payment Amount'].std()
print('Standard Deviation of Payment',std_payment)
#%%
summary = df.describe()
print(summary)





