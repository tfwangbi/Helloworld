# POST request
import time

import requests
from fake_useragent import UserAgent
import json

# url = 'https://www.iciba.com/translate'
# https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_new_fanyi&sign=aG5ry6oF%2BIvstLPiNdhDiNRriqVIAJSQ%2BxmfU0q7dIE%3D

# req = requests.post(url, data)
post_cb_url = 'https://ifanyi.iciba.com/index.php?c=trans'
headers = {
    'User-Agent': UserAgent().random
}


# 金山翻译 start -
# word = input("Input a word to translate to English: ")
#
# data = {
#     'from' : 'zh',
#     'to' : 'en',
#     'q' : word
# }
#
# res = requests.post(post_cb_url, headers=headers, data=data)
# print(f'The English is: ' + json.loads(res.text)['out'])

# 金山翻译 end -

class Cbtranslate:
    def __init__(self):
        self.url = post_cb_url
        self.headers = {
            'User-Agent': UserAgent().random
        }

    def _send_post(self, data):
        res = requests.post(self.url, headers=self.headers, data=data)
        time.sleep(1)
        return res.text

    @staticmethod
    def _output_result(text):
        result_dic = json.loads(text)
        print(f'The translate result is: ' + result_dic['out'] + '.')

    def run(self, data):
        d = self._send_post(data)
        self._output_result(d)


# Cookies handle starts
# requests.session()


if __name__ == "__main__":
    word = input("Input words to translate to English: ")
    data = {
        'from': 'zh',
        'to': 'ja',
        'q': word
    }

    ts = Cbtranslate()
    ts.run(data)
