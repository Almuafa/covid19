# COVID19
Web Scraping COVID19 data from public websites using BeautifulSoup

## Workflow
Description of python scripts and python modules used as part of this workflow

Below are the scripts used
- `covid.py`
- `pull.py`
### covid.py
This script consists of modules that will called by the [`pull.py`](pull.py) script, such as
- pull_states
- pull_state_data_by_date
- pull_state_data_by_county

#### pull_states
This function pulls all the states which will be used by other modules

#### pull_state_data_by_date
This function pulls the data by state as argument and returns a dataframe

#### pull_state_data_by_county
This function pulls the data by county as argument and returns a dataframe

### pull.py
This script is the main orchestrator which uses [`covid.py`](covid.py) and its modules to pull the data from the public websites.

## Usage
Please run the script using the following command

```python
python pull.py
```
*alternatively you can run the jupyter notebook `covid19.ipynb` included as part of the repo*

## References
This repo used the following references in coming up with all code etc.,
- https://docs.python.org/3/library/functions.html#open
- https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States
- https://pandas.pydata.org/
- https://pypi.org/project/beautifulsoup4/
- https://docs.python.org/3.0/library/functions.html?highlight=super
- https://www.w3schools.com/python/python_lists.asp
## Feedback
Please create GitHub issues, if you find any issues or bugs or ideas to improve upon