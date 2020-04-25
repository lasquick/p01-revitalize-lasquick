# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:11:39 2020

@author: lasqu
"""

import pandas as pd
pd.set_option('display.max_rows',None)

#Uses CSV to identify desired poverty information grouping.
var_info = pd.read_csv('povstat.csv', index_col='variable')
var_group = var_info['group']
print(var_group)

#Pulls in CSV of Census data capture.
results = pd.read_csv('census-povstat.csv', index_col='NAME')

#Removes Puerto Rico from data.
results = results[results.state != 72]

#Uses grouping convention to group Census data.
group_by_level = results.groupby(var_group, axis='columns', sort=False)
by_level = group_by_level.sum()
levels = ['totalpop', 'totalpovpop', '<pov']

#Compute the percent of the population in each aggregate group.
pct = 100*by_level.div(by_level['totalpovpop'],axis='index')
results['pctpov'] = pct['<pov']

#Provides samples of ratio data for counties.
#Identifies top 10.
top10 = pct['<pov'].sort_values(ascending=False)
top10 = top10.iloc[0:10]
print(top10)


#Creates geoid variable from concatenating state and county variables.
results['state'] = results['state'].astype(str).str.zfill(2)
results['county'] = results['county'].astype(str).str.zfill(3)
results['geoid'] = results['state'].astype(str)+results['county'].astype(str)

#Saves top 10 poverty counties for local-level analysis.
#results['pctpov'] = pct['<pov']
povtop10 = results[results['pctpov'].isin(top10)]
povtop10.to_csv('povtop10.csv')


#Uses dictionary to rename variable.
newnames = {'B01003_001E':'totalpop', 'B17001_001E':'totalpovpop',
            'B17001_002E': '<pov'}
results.rename(newnames,axis='columns', inplace=True)
results['geoid'] = results['geoid'].astype(str)
results.to_csv('povstat-map.csv')