# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:33:22 2020

@author: lasqu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

#Reads in csv data.
pov18 = pd.read_csv('povstat-map.csv', index_col='NAME')
pov12 = pd.read_csv('povstat-map-12.csv', index_col='NAME', dtype=str)

#Retains only important fields from committee info file.
#com_info = com_info[['CMTE_ID', 'CMTE_NM', 'CMTE_PTY_AFFILIATION', 'CAND_ID']]

#Merges committee info and totals data.
pov_merged = pov12.merge(pov18, how='right', on='NAME', validate='m:1', indicator=True)
print(pov_merged['_merge'].value_counts())
pov_merged.drop(['_merge'], axis='columns', inplace=True)

# _x variables for 2012 data; _y variables for 2018 data.
pov_merged['changepov'] = pov_merged['pctpov_y'] - pov_merged['pctpov_x'].astype(float)

#Identifies top 10 counties increase in poverty.
top10 = pov_merged['changepov'].sort_values(ascending=False)
top10 = top10.iloc[0:10]
print('Top 10 counties by increase in percent poverty:', top10)

#Identifies top 10 counties decrease in poverty.
bottom10 = pov_merged['changepov'].sort_values(ascending=True)
bottom10 = bottom10.iloc[0:10]
print('Top 10 counties by decrease in percent poverty:', bottom10)


#Uses distributional analysis to separate poverty changes by population segments.
pov_merged['totalpop_y'].astype(float).describe()
bin_values = np.arange(start=0, stop=1000000, step=5000)
pov_merged['totalpop_y'].hist(bins=bin_values, figsize=[14,6])

#Identifies the top 3 counties with the largest poverty percentage point
#increases and decreases by county population thresholds.
poplow = pov_merged[pov_merged.totalpop_y < 5000]
top3 = poplow['changepov'].sort_values(ascending=False)
top3 = top3.iloc[0:3]
print('\nTop 3 <5k pop counties by increase in percent poverty:', top3)
bottom3 = poplow['changepov'].sort_values(ascending=True)
bottom3 = bottom3.iloc[0:3]
print('\nTop 3 <5k pop counties by decrease in percent poverty:', bottom3)


pop5k = pov_merged[pov_merged.totalpop_y >= 5000]
top3 = pop5k['changepov'].sort_values(ascending=False)
top3 = top3.iloc[0:3]
print('\nTop 3 5k+ pop counties by increase in percent poverty:', top3)
bottom3 = pop5k['changepov'].sort_values(ascending=True)
bottom3 = bottom3.iloc[0:3]
print('\nTop 3 5k+ pop counties by decrease in percent poverty:', bottom3)


pop10k = pov_merged[pov_merged.totalpop_y >= 10000]
top3 = pop10k['changepov'].sort_values(ascending=False)
top3 = top3.iloc[0:3]
print('\nTop 3 10k+ pop counties by increase in percent poverty:', top3)
bottom3 = pop10k['changepov'].sort_values(ascending=True)
bottom3 = bottom3.iloc[0:3]
print('\nTop 3 10k+ pop counties by decrease in percent poverty:', bottom3)


pop50k = pov_merged[pov_merged.totalpop_y >= 50000]
top3 = pop50k['changepov'].sort_values(ascending=False)
top3 = top3.iloc[0:3]
print('\nTop 3 50k+ pop counties by increase in percent poverty:', top3)
bottom3 = pop50k['changepov'].sort_values(ascending=True)
bottom3 = bottom3.iloc[0:3]
print('\nTop 3 50k+ pop counties by decrease in percent poverty:', bottom3)


pop100k = pov_merged[pov_merged.totalpop_y >= 100000]
top3 = pop100k['changepov'].sort_values(ascending=False)
top3 = top3.iloc[0:3]
print('\nTop 3 100k+ pop counties by increase in percent poverty:', top3)
bottom3 = pop100k['changepov'].sort_values(ascending=True)
bottom3 = bottom3.iloc[0:3]
print('\nTop 3 100k+ pop counties by decrease in percent poverty:', bottom3)


#Distributional analysis of changes in poverty rates.
bin_values = np.arange(start=-30, stop=30, step=1)
pov_merged['changepov'].hist(bins=bin_values, figsize=[14,6])


#Relationship between change in population and change in poverty.
pov_merged['totalpop_x'] = pov_merged['totalpop_x'].astype(float)
pov_merged['totalpop_y'] = pov_merged['totalpop_y'].astype(float)
pov_merged['changepop'] = (pov_merged['totalpop_y'] - pov_merged['totalpop_x']) / pov_merged['totalpop_x']
plt.scatter(pov_merged['changepop'], pov_merged['changepov'], marker='o')


#Exports merged comparison data to CSV file to map.
pov_merged.to_csv('povstat-12-18-map.csv',header=True)