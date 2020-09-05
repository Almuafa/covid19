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
    """
    name: pull_state_data_by_county
    desc: this function pulls the data by state as argument and returns a dataframe
    
    input: state (name of the state, for ex., Texas)
    output: dataframe (pandas dataframe)
    
    example invocation: 
        dataframe = pull_state_data_by_county('Texas')
    """
    # building url
    link = requests.get(f'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_{state}').text

    # parsing the page and the data
    soup_county =bs(link_county , "html.parser")
    table_county = soup_county.find('div', attrs={"class" :"tp-container"})
    rows = table_county.find("tbody").find_all('tr') 
    
    # get the header columne 
    header = []
    for head in heads:
        col1 = heads[0].text.replace("\n", "")
        if col1 not in header:
            header.append(col1)
        col2 = heads[1].text.replace("\n", "")
        if col2 not in header:
            header.append(col2)
        col3 = heads[2].text.replace("\n", "")
        if col3 not in header:
            header.append(col3)
        col4 = heads[3].text.replace("\n", "")
        if col4 not in header:
            header.append(col4)
        col5 = heads[4].text.replace("\n", "")
        if col5 not in header and not col5.lower().startswith('cas'):
            header.append(col5)

    # to get the position of headers
    count = 0
    for l in header:

        if l.lower().startswith('c'):
            position_of_case = count
        elif l.lower().startswith('pop'):
            position_of_pop = count
        elif l.lower().startswith('dea'):
            position_of_death = count
        elif l.lower().startswith('cou'):
            position_of_county = count
        count += 1
    # get the conutyes and remove the None 
    rows_county = table_county.find("tbody").find_all('a')
    counties = []
    co = []
    for r in rows_county:
        co.append(r.get('title'))

    # list of counties
    for c in co:
        if c is not None:
            d = c.split("County")[0]
            counties.append(d)

    # extract county, confirmed, deaths, pupulation from the record by looping thru them
    # data_county = []
    # for row in rows:
    #     county = row.find('a').text
    #     cases = row.find_all('td')[0].text.replace("\n", "")
    #     deaths = row.find_all('td')[2].text.replace("\n", "")
    #     pupulation = row.find_all('td')[3].text.replace("\n", "")
    #     data_county.append((county, cases, deaths , pupulation))

    # create dataframe
    df_county = pd.DataFrame(data_county ,columns=['county', 'cases', 'deaths' , 'pupulation'])

    # add state column
    df_county['state'] = f'{state}'
 
    return df_county