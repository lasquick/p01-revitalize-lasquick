# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:25:37 2020

@author: lasqu
"""

import requests
import pandas as pd

#Uses CSV file with Census data variable names to create data pull request.
var_info = pd.read_csv('povstat.csv')
var_name = var_info['variable'].to_list()
var_list = ['NAME']+var_name
var_string = ','.join(var_list)

#Sets API observation capture conditions and sets API key.
api = 'https://api.census.gov/data/2012/acs/acs5'
for_clause = 'county:*'
in_clause = 'state:*'
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
attain.to_csv('census-povstat-12.csv')
    