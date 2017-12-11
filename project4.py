# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:58:49 2017

@author: laksh
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
df =pd.read_csv('CleanedData.csv',index_col=0,dtype={'Hospice Beneficiaries':'float64'})

df2 = dict(zip(df['Average Age'], df['Total Live Discharges']))

lists = sorted(df2.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

matplotlib.style.use('ggplot')


plt.scatter(x, y,color='Red')
plt.title('Relationship between Average age and Total Live Discharges')
plt.xlabel('Age')
plt.ylabel('Total Live Discharges')
plt.show()