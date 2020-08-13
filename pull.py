from bs4 import BeautifulSoup as bs
import requests
r = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States').text
suop = bs(r , 'lxml')
title = suop.title.string
results = suop.find_all('tr' , attrs={"class":"mw-collapsible"})
records = []
for result in results:
    date = result.contents[1].text
    confirmed = result.find('span' , class_="cbs-ibr").text
    deaths = result.contents[-2].text
    records.append((date, confirmed, deaths))

records
import pandas as pd 
df = pd.DataFrame(records , columns=['date' ,'confirmed' ,'deaths'])
df['date'] = pd.to_datetime(df['date'] , errors='coerce')
df.to_csv("Desktop/COVID-19 pandemic in the USA - Wikipedia.csv" , index=False , encoding='utf-8')