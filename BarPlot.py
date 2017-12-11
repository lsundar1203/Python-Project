# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:10:18 2017

@author: laksh
"""
import pandas as pd
#import pylab as plt
import matplotlib
import matplotlib.pyplot as plt
df =pd.read_csv('CleanedData.csv',index_col=0,dtype={'Hospice Beneficiaries':'float64'})


#plt.bar( df['State'],df['Hospice Beneficiaries'])
#df1 = pd.DataFrame(df2.groupby(['Hospice Beneficiaries','Total Live Discharges']))

df['Percentage']=df['Total Live Discharges']/df['Hospice Beneficiaries']*100
df2 = df[['Name','Percentage']]
top25 = df2.sort_values('Percentage',ascending=0).head(25)[['Percentage', 'Name']]
#print(df.dtypes)
#plt.bar(df['Percentage'], df['Name'], align='center')
#plt.xtics(df['Name'] )
#plt.show()
plt.rcParams['figure.figsize']=(10,6)
matplotlib.style.use('ggplot')
#print(plt.style.available)
#x_ticks_label=[['Name']]
#top25.plot(kind='bar')
ax=top25.plot.bar(x='Name', y='Percentage',title='Top 25 Hospice Providers in the US according to Percentage of Live Discharges')
#print(top25)
#for i in ax.patches:
 #   ax.text(i.get_x()+.12, i.get_height()-3,list_25+'%', fontsize=22, color='white')