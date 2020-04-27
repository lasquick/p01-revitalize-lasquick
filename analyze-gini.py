# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:11:39 2020

@author: lasqu
"""
#This file cleans county Gini coefficient and quantile income shate data 
#and identifies the top ten counties with the highest Gini coefficients. The 
#resulting CSV file is used to map county level inequality data.

import pandas as pd
pd.set_option('display.max_rows',None)

#Uses CSV to identify desired poverty information grouping.
var_info = pd.read_csv('variables/gini.csv', index_col='variable')
var_group = var_info['group']
print(var_group)

#Pulls in CSV of Census data capture.
results = pd.read_csv('census/census-gini.csv', index_col='NAME')

#Removes Puerto Rico from data.
results = results[results.state != 72]

#Uses dictionary to rename variable.
newnames = {'B19083_001E':'gini', 'B19082_001E':'Q1', 'B19082_002E':'Q2', \
            'B19082_003E':'Q3', 'B19082_004E':'Q4', 'B19082_005E':'Q5', \
            'B19082_006E':'Top5'}
results.rename(newnames,axis='columns', inplace=True)

#Uses grouping convention to group Census data.
group_by_level = results.groupby(var_group, axis='columns', sort=False)
by_level = group_by_level.sum()
#levels = ['gini', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Top5']

#Identifies top 10 counties with highest Gini coefficients.
top10 = results['gini'].sort_values(ascending=False)
top10 = top10.iloc[0:10]
print(top10)

#Creates geoid variable from concatenating state and county variables.
results['state'] = results['state'].astype(str).str.zfill(2)
results['county'] = results['county'].astype(str).str.zfill(3)
results['geoid'] = results['state'].astype(str)+results['county'].astype(str)


#Exports to CSV file.
results['geoid'] = results['geoid'].astype(str)
results.to_csv('mapfile/gini-map.csv')
