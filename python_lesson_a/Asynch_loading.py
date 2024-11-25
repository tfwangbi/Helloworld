'''
Asynchro loading
'''
import json

import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath
from lxml import etree

# url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
headers = {
    'User-Agent': UserAgent().random
}

# res = requests.get(url, headers=headers)
# jdata = json.loads(res.text)

# movie_dic = {}

# m_name, m_rate = jsonpath(jdata, '$..title'), jsonpath(jdata, '$..rate')
#
# move_dic = zip(m_name, m_rate)
# print(dict(move_dic))

# for name, rate in m_name, m_rate:
#     movie_dic['title'] = name
#     movie_dic['rate'] = rate
#
# moive = []
#
# for i in range(len(m_name)):
#     # print(m_name[i])
#     movie_dic = {'title': m_name[i], 'rate': m_rate[i]}
#
#     moive.append(movie_dic)
#     # print(movie_dic)
#

url = 'https://movie.douban.com/top250?'

res = requests.get(url, headers=headers)
# print(res.text)

html = etree.HTML(res.text)
movie_name = html.xpath('//div[@class="hd"]/a/span[1]/text()')
movie_rate = html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/div/span[2]/text()')

move_list = dict(zip(movie_name, movie_rate))

print(move_list)




