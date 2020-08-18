#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# In[2]:


# from covid import pull_recent_state_data # redudant
from covid import pull_state_data_by_date
from covid import pull_state_data_by_county


# In[3]:


# unit testing
# dataframe = pull_state_data_by_date('Alabama')
# dataframe.head()


# In[4]:


# reading states
states = open('states.lst', 'r').read().split(',')

# pull the states data by looping through the list
for state in states:
    state = state.lstrip()
    print(f'pulling data for state: {state}')
    df = pull_state_data_by_date(state)
    
    print(f'writing to csv, for state: {state}')
    df.to_csv(f'data\\{state}.csv', index=False)
    print(f'file written to: data\\{state}.csv')
    print('')

# load the csv files into database
# in the database, there will 2 tables
# states (date, state, case, death)
#   jan 1st 2020, TX, 123,123
#   Jan 1st 2020, AL, 34, 234
# counties (state, county, case, death, population)


# query




# from bs4 import BeautifulSoup as bs
# import requests
# import pandas as pd 

# # COVID-19 pandemic in the USA by date- Wikipedia

# r = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States').text
# suop = bs(r , 'lxml')
# title = suop.title.string
# results = suop.find_all('tr' , attrs={"class":"mw-collapsible"})
# records = []
# for result in results:
#     date = result.contents[1].text
#     confirmed = result.find('span' , class_="cbs-ibr").text
#     deaths = result.contents[-2].text
#     records.append((date, confirmed, deaths))

# records

# ##### get a data to the pandas to get data frame

# df = pd.DataFrame(records , columns=['date' ,'confirmed' ,'deaths'])
# df['date'] = pd.to_datetime(df['date'] , errors='coerce')
# df.to_csv("Desktop/COVID-19 pandemic in the USA - Wikipedia.csv" , index=False , encoding='utf-8')

# # COVID-19 pandemic in the United States by state and territory

# link = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States').text
# soup1=bs(link , "html.parser")
# table = soup1.find('table', attrs={"class" : "wikitable"})
# rows = table.select("tbody tr")[3:-3]

# data = []
# for row in rows:
#     state = row.find_all('th' , attrs = {'scope' : 'row'})[1].find('a').text
#     cases = row.find_all('td')[0].text.replace("\n", "")
#     deaths = row.find_all('td')[1].text.replace("\n","")
#     recoveries = row.find_all('td')[2].text.replace("\n","")
#     data.append((state, cases, deaths , recoveries))

# ##### get a data to the pandas to get data frame

# df1 = pd.DataFrame(data , columns=['state', 'cases', 'deaths' , 'recoveries'])
# df1.to_csv("Desktop/COVID-19 pandemic in the USA by states.csv" , index=False )

