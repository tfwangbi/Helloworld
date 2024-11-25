import requests
from fake_useragent import UserAgent
from retrying import retry

url = 'https://www.baidu.com'
ck_url = 'https://2024.ip138.com/'

headers = {
    'User-Agent': UserAgent().random
}


# proxies = {
#     'https': '120.196.207.10:80'
# }
#
# res = requests.get(ck_url, headers=headers, proxies=proxies)
#
# print(res.text)


# # retrying module starts
# @retry(stop_max_attempt_number=3)
# def test():
#     print('123')
#
#
# try:
#     test()
# except:
#     print('fail')
# # retrying module end

# timeout starts


proxies = {
    'https': '120.196.207.10:80'
}

res = requests.get(ck_url, headers=headers, proxies=proxies, timeout=1)

print(res.text)