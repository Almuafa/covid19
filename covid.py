import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def pull_states():
    """
    name: pull_states
    desc: this function pulls all the states which will be used by other modules
    
    input: None
    output: list (list of all states)
    
    example invocation: 
        states = pull_states()
    """
    link = requests.get('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States').text
    soup = bs(link , "html.parser")
    table = soup.find('table', attrs={'class': 'wikitable', 'class': 'sortable'})
    rows = table.select("tbody tr")[3:-3]
    states = []
    for row in rows:
        state = row.find_all('th' , attrs = {'scope' : 'row'})[1].find('a').text.replace(" ", "_")
        states.append(state)
    return states
    
def pull_state_data_by_date(state):
    """
    name: pull_state_data_by_date
    desc: this function pulls the data by state as argument and returns a dataframe
    
    input: state (name of the state, for ex., Texas)
    output: dataframe (pandas dataframe)
    
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
    """
    name: pull_state_data_by_county
    desc: this function pulls the data by county as argument and returns a dataframe
    
    input: state (name of the state, for ex., Texas)
    output: dataframe (pandas dataframe)
    
    example invocation: 
        dataframe = pull_state_data_by_county('Texas')
    """
    # building url
    url = f'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_{state}'
    r = requests.get(url)
    # parsing the page and the data
    soup = bs(r.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable', 'class': 'sortable'})
    
    # read the table and create dataframe
    df_county = pd.read_html(str(table))
        
    return df_county[0]