# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:11:39 2020

@author: lasqu
"""
#This file requires a single input change--county rank-- to compile exploratory
#analyses of census tract-level demographic data for top poverty counties.
#The script prints ranked variable lists, generates charts, and exports a CSV
#file to be used for mapping data prepared in this file.

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows',None)

#!!IMPORTANT!! CHANGE TO APPROPRIATE LIST AND RANKING
countyrank = 'povtop10-1'


#Uses CSV to identify desired poverty information grouping.
var_info = pd.read_csv('variables/county.csv', index_col='variable')
var_group = var_info['group']
print(var_group)

#Pulls in CSV of Census data capture.
#NOTE: Would be useful to add file name for loop to loop all top 10 files.
results = pd.read_csv('census/census-'+countyrank+'.csv', index_col='NAME')

#Uses grouping convention to group and rename Census variables.
group_by_level = results.groupby(var_group, axis='columns', sort=False)
by_level = group_by_level.sum()
levels = ['totalpop','totalpovpop','<pov','income','medinc','Q1','Q2','Q3',\
          'Q4','Q5','Top5','total-incpovrat','<.50','.50-.99','1.00-1.24',\
          '1.25-1.49','1.50-1.84','1.85-1.99','2.00+','total-tenure','owner',\
          'renter','total-employment','laborforce','civillaborforce','employed',\
          'unemployed','military','non-labor','total-hhincome','native',\
          'foreign','total-race','white','black','nativeamer','asianpac',\
          'other','multiracial','total-hispanic','nonhispanic','hispanic']


#Adds basic computation for key demographic data.
by_level['unemployment'] = 100*by_level['unemployed']/by_level['civillaborforce']
print('\nUnemployment Rates:',by_level['unemployment'].sort_values(ascending=False).round(2))

by_level['incpercap'] = by_level['income']/by_level['totalpop']
print('\nIncome per Capita:',by_level['incpercap'].sort_values(ascending=True).round(2))

by_level['homeownership'] = 100*by_level['owner']/by_level['total-tenure']
print('\nTenant Homeownership Rates:',by_level['homeownership'].sort_values(ascending=True).round(2))

by_level['immigrant']=by_level['foreign']/by_level['totalpop']
print('\nPercent Foreign Born:',by_level['immigrant'].sort_values(ascending=False).round(2))

by_level['pctpov'] = 100*by_level['<pov']/by_level['totalpovpop']
print('\nPoverty Rates:',by_level['pctpov'].sort_values(ascending=False).round(2))


#Basic Visualizations of Poverty Data
sns.set(style='white')

#Histogram of poverty rates by census tracts.
plt.figure()
fg = sns.distplot(by_level['pctpov'])
plt.savefig('visualizations/'+countyrank+'_pctpov.png')

plt.figure()
fg = sns.distplot(by_level['medinc'])
plt.savefig('visualizations/'+countyrank+'_medinc.png')

plt.figure()
fg = sns.distplot(by_level['unemployment'])
plt.savefig('visualizations/'+countyrank+'_unemployment.png')

jp = sns.jointplot('pctpov','totalpop',data=by_level,kind='hex')
jp.savefig('visualizations/'+countyrank+'pctpov_by_pop.png')

#Creates geoid variable from concatenating state, county, and tract variables.
results['state'] = results['state'].astype(str).str.zfill(2)
results['county'] = results['county'].astype(str).str.zfill(3)
by_level['geoid'] = results['geoid'] = results['state']+results['county']+results['tract'].astype(str)

#Exports to CSV for mapping.
by_level.to_csv('mapfile/'+countyrank+'-map.csv')