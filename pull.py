import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from covid import pull_state_data_by_date, pull_state_data_by_county, pull_states

### Get the states names and write them to a list file.

states = pull_states()
with open('data\states.lst', 'w') as file_handler:
    for state in states:
        file_handler.write(f'{state},\n')

### Get cases for state by date

states = open('data\states.lst', 'r').read().split(',')

for state in states:
    state = state.lstrip()
    print(f'pulling data for state: {state}')
    try:
        df = pull_state_data_by_date(state)
    except:
        print(f'skipping {state}, since its erroring...')
    
    print(f'writing to csv, for state: {state}')
    df.to_csv(f'data\{state}.csv', index=False)
    print(f'file written to: {state}.csv')
    print('')


### Get cases for state by county

states = open('data\states.lst', 'r').read().split(',')

for state in states:
    state = state.lstrip()
    print(f'pulling data for state: {state}')
    try:
        df = pull_state_data_by_county(state)
    except:
        print(f'{state} is skipped, due to errors')
    
    print(f'writing to csv, for state: {state}')
    df.to_csv(f'data\{state}county.csv', index=False)
    print(f'file written to: {state}.csv')
    print('')

