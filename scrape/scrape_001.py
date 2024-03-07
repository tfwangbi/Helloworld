import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

html = requests.get('https://www.baidu.com/', headers=headers).text

soup = BeautifulSoup(html, 'html.parser')

all_hot_search = soup.findAll('li', attrs = {'class':'hotsearch-item'})
for hot_search in all_hot_search:
    spans = hot_search.findAll('span')
    for span in spans:
        if 'title-content-index' in span.attrs("class"):
            print(span.string)

