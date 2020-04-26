# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:25:37 2020

@author: lasqu
"""
#This file completes a manual Census API request for each county on a given 
#list. Change the county list and rank here and the rest of the file will 
#automatically run and export a CSV to be used in the accompanying analyze file.

import requests
import pandas as pd

#!!IMPORTANT: CHANGE TO CORRECT POVERTY RANKING LIST AND COUNTY RANK!!
county_list = 'povtop10'
county_rank = '1'

#Uses CSV file with Census data variable names to create data pull request.
var_info = pd.read_csv('county.csv')
var_name = var_info['variable'].to_list()
var_list = ['NAME']+var_name
var_string = ','.join(var_list)

county_info = pd.read_csv(county_list+'.csv')

#Create in_list to identify top ten counties' county and state IDs.
in_list = ('county:'+county_info['county'].astype(str).str.zfill(3)+' state:'\
           +county_info['state'].astype(str).str.zfill(2))
print(in_list)
index_rank = int(county_rank)-1


#Sets API observation capture conditions and sets API key.
api = 'https://api.census.gov/data/2018/acs/acs5'
for_clause = 'tract:*'
in_clause = in_list[index_rank]
key_value = '7106dbed1eb3f120e22e544652313d756577a258'


#Runs to API request using set up provided above. Indicates success or error.
payload = {'get':var_string, 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)
if response.status_code == 200:
    print('\nSuccess!')
else:
    print(response.status_code, response.text)
    assert False

#Converts Census JSON to dataframe and labels variables.
row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]
attain = pd.DataFrame(columns=colnames, data=datarows)

#Sets name as the index and writes to CSV file.
attain.set_index('NAME', inplace=True)
attain.to_csv('census-'+county_list+'-'+county_rank+'.csv')