# print("Hello world")

import requests


url = 'https://movie.douban.com/top250'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
if response.ok:
    print(response.text)
else:
    print("Request fail")

# print(response)
# print(response.status_code)