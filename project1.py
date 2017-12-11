# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:59:50 2017

@author: laksh
"""

import pandas as pd


# importing csv
df =pd.read_csv('MedicareHospiceCare.csv')

df1= pd.read_csv('MedicareHospiceCare.csv')

#Removing NaN values
df1.fillna(0,inplace = True)


#deleting unwanted columns
df1.drop(df1.columns[31:48], axis=1, inplace=True)

df1.drop(df1.columns[18:24],axis=1,inplace= True)

df1.drop(df1.columns[13],axis=1,inplace =True)

df1.drop(df1.columns[3],axis =1, inplace =True)


#Splitting columns 
df1[['HRR','HRRCity']]=df1['HRR'].str.split(' - ',expand=True)


df1.to_csv('CleanedData.csv')

