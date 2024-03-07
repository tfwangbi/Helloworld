import requests
import random
from fake_useragent import UserAgent
from urllib.parse import quote, unquote

url = 'https://www.baidu.com'
url_suffix = '/s?'
m_url = 'http://www.pop-photo.com.cn/data/attachment/forum/202001/12/155651pyu64t35y3ly5dl8.jpg'

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

# 请求池 way 1
# UAList = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
#     'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
#     'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
# ]
#
# print(random.choice(UAList))

# way 2
# print(UserAgent().random)

headers = {}
headers['User-Agent'] = UserAgent().random

# wd = '学习'

# 构建参数字典
name = input('Please input the key word to search: ')
kw = {'wd': name}

# print(url + f'/s?wd={quote(wd)}')

response = requests.get(url + url_suffix, headers=headers, params=kw)

print(response.content.decode())

# print(response.headers)

# with open('../../download/image_001/{}.jpg'.format("chunse001"), 'wb') as f:
#     f.write(response.content)
#
# print('Picture download done')
# save picture

# quote 明文转密文
# unquote 密文转明文

# print(quote("学习"))  # %E5%AD%A6%E4%B9%A0
# print(unquote('%E5%AD%A6%E4%B9%A0'))  # 学习

# send url with parameters
