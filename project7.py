# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 10:36:59 2017

@author: Heart BEAT'S
"""

import pandas as pd
import numpy as np
#import pylab as plt
import matplotlib
import matplotlib.pyplot as plt
df =pd.read_csv('CleanedData.csv',index_col=0,dtype={'Hospice Beneficiaries':'float64'})
#print(df.dtypes)
state_count=df.groupby(['State']).size().reset_index(name='count')
print(state_count)
nparray_count=state_count['count'].values
#print(nparray_count)
list_count=np.array(nparray_count).tolist()
#print(list_count)#list of count

nparray_state=state_count['State'].values
#print(nparray_state)
list_state=np.array(nparray_state).tolist()
#print(list_state)#list of states
plt.rcParams['figure.figsize']=(12,8)
#print(plt.style.available)
matplotlib.style.use('seaborn-bright')
plt.barh(list_state,list_count,color='orange')
plt.title('Horizontal Bar chart showing Hospice providers per state')
plt.show()