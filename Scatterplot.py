# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 06:33:08 2017

@author: Heart BEAT'S
"""

import pandas as pd
#import pylab as plt
#import matplotlib
#import matplotlib.pyplot as plt
df =pd.read_csv('CleanedData.csv',index_col=0,dtype={'Hospice Beneficiaries':'float64'})
#print(df.dtypes)
df.plot.scatter('Skilled Nursing Visit Hours per Day','Total Live Discharges',s=100,color='purple',title='Relationship between Live Discharges and Skilled Nursing visit hours per day')