import requests
from lxml import etree

url = 'https://image.baidu.com/search/index?ct=201326592&tn=baiduimage&word=%E6%98%A5%E5%A4%A9%E5%9B%BE%E7%89%87%E5%94%AF%E7%BE%8E&pn=&spn=&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&cs=&os=&objurl=&di=&gsm=5a'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

html = requests.get(url, headers=headers).text
selectors = etree.HTML(html)
all_image_url = selectors.xpath('//img[@class="main_img"]/@src')

print(all_image_url)
