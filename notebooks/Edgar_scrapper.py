# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

from ratelimit import limits, sleep_and_retry


class EdgarAccess(object):

    @staticmethod
    @sleep_and_retry
    # Dividing the call limit by half to avoid coming close to the limit
    @limits(calls=5, period=1)
    def get(url,is_json=False):
        if is_json:
            return requests.get(url).json()
        else:
            return requests.get(url).text

'''
edgar_access = EdgarAccess()

url = "https://data.sec.gov/submissions/CIK0001018724.json"
print(edgar_access.get(url,True))

def get_fillings(fillings_cik, doc_type, start=0, count=60):
    fillings_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}\
            &type={}&start={}&count={}&owner=exclude&output=atom'.format(fillings_cik, doc_type, start, count)
    fillings_html = edgar_access.get(fillings_url)
    fillings_soup = BeautifulSoup(fillings_html, features="html.parser")

    fillings_list = [
        (link.find('filing-href').getText(),
         link.find('filing-type').getText(),
         link.find('filing-date').getText())
        for link in fillings_soup.find_all('entry')]

    return fillings_list


ticker_ciks = pd.read_csv('tickers.csv')

sec_fillings = {}

for ticker, cik in ticker_ciks[:2].values:
    sec_fillings[ticker] = get_comp_fillings(cik, '10-K')
    #print(sec_fillings[ticker])

fillings_doc_raw = {}
for ticker, data in sec_fillings.items():
    fillings_doc_raw[ticker] = {}
    for filing_href, filing_type, filing_date in tqdm(data, desc='Downloading {} Fillings'.format(ticker), unit='filling'):
        if (filing_type == '10-K'):
            file_url = filing_href.replace('-index.htm', '.txt').replace('.txtl', '.txt')
            fillings_doc_raw[ticker][filing_date] = edgar_access.get(file_url)
            link.find('DOCUMENT').getText()

'''