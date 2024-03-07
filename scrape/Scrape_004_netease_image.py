import requests
import time
from fake_useragent import UserAgent

file_path = '../../download'
file_path_img = '/image_001'
file_name = 'Music picture'
headers = {}
headers['User-Agent'] = UserAgent().random

# Get a picture
img_url = 'https://p1.music.126.net/9OUqMH5LAOh841Jn3Y0ulQ==/109951169388184078.jpg'
music_url = 'https://m801.music.126.net/20240306163605/2332e5d3c53271757279dc26178f5280/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/7284218484/fe3a/edac/1714/45970349e682a5c1a3a3bd652e2ea463.m4a'

res = requests.get(img_url, headers=headers)
# print(res.content)


present_time = str(int(time.mktime(time.localtime())))
# print(present_time)

with open(file_path + file_path_img + f'/{file_name}_{present_time}.jpg', 'wb') as f:
    f.write(res.content)

print('picture download done.')

# Get a Song


# Get a Music Moive
