import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def pull_state_data_by_date(state):
    """
    name: pull_state_data_by_date
    desc: this function pulls the data by state as argument and returns a dataframe
    
    input: state (name of the state, for ex., Texas)
    output: dataframe (pandas dataframe)
    
    output: date, state, cases, death
    
    example invocation: 
        dataframe = pull_state_data_by_date('Texas')
    """
    
    # building url
    link = requests.get(f'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_{state}').text
    
    # parsing the page
    soup = bs(link , 'lxml')
    results = soup.find_all('tr', attrs={"class":"mw-collapsible"})
    
    # extract date, confirmed, deaths from the record by looping thru them
    records = []
    for result in results:
        date = result.contents[1].text
        confirmed = result.find('span', class_="cbs-ibr").text
        deaths = result.find_all('span', class_="cbs-ibr")[1].text
        records.append((date, confirmed, deaths))
    
    # create dataframe
    df = pd.DataFrame(records , columns=['date' ,'confirmed' ,'deaths'])
    
    # converting date to date format
    df['date'] = pd.to_datetime(df['date'] , errors='coerce')
    
    # add state column
    df['state'] = f'{state}'
 
    return df

def pull_state_data_by_county(state):
    # not cmplemented
    return None