import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

# url = 'https://www.baidu.com/'
# url = 'https://httpbin.org/post'
index_url = 'https://tieba.baidu.com/p/5624001749'
data = {
    'wd': "python"
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


# request = requests.post(url, headers=headers, data=data)
# request.encoding = 'utf-8'

html = requests.get(index_url, headers=headers).text
# print(html)

#lxml application
selectors = etree.HTML(html)
image_urls = selectors.xpath('//img[@class="BDE_Image"]/@src')
# print(image_urls)

offset = 'spring'
n = 1
for img_url in image_urls:

    # print(img_url)
    image_content = requests.get(img_url).content
    # print(image_content)

    with open('../../download/image_001/{}.jpg'.format(offset + f"{n}"), 'wb') as fw:
        fw.write(image_content)

    print(f'Download image {n} done')
    n = n + 1

    time.sleep(1)

