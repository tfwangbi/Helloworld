import time
import requests
from fake_useragent import UserAgent

# https://tieba.baidu.com/f?kw=%E4%BB%BB%E8%B4%A4%E9%BD%90&ie=utf-8&pn=0 page 1
# https://tieba.baidu.com/f?kw=%E4%BB%BB%E8%B4%A4%E9%BD%90&ie=utf-8&pn=50 page 2
# https://tieba.baidu.com/f?kw=%E4%BB%BB%E8%B4%A4%E9%BD%90&ie=utf-8&pn=100 page 3

'''
'''
addr = 'tieba'
star_name = 'xiaoqi'
headers = {}
headers['User-Agent'] = UserAgent().random
headers['Referer'] = 'https://wappass.baidu.com/'

file_path = '../../download'
file_path_file = '/htmlfiles_001'

# url construct

base_url = 'https://tieba.baidu.com/f?'


# kw = input('Please input a word to start download files from tieba: ')

# for i in range(4):
#     # print(i * 50)
#
#     params = {
#         'kw' : kw,
#         'pn' : i * 5
#     }
#
#     # url = base_url + f'kw={str(kw)}&pn={i*50}'
#
#     # print(url)
#     res = requests.get(base_url, headers=headers, params=params)
#     time.sleep(1)
#     filename = file_path + file_path_file + '/' + addr + '_' + kw + '_' + str(i + 1) + '.html'
#
#
#     with open(filename, 'wb') as f:
#         f.write(res.content)
#
#     print(f'Page {i + 1} completed.')
#     time.sleep(1)

class Tieba:
    def __init__(self):
        self.url = base_url
        # self.headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        # }
        # self.headers['User-Agent'] = UserAgent().random
        self.headers = {
            'User-Agent': UserAgent().random,
            'Cookie': 'BIDUPSID=56E7AD86AA3B7C0355E9993C555DE4E3; PSTM=1709039875; BAIDUID=56E7AD86AA3B7C032C167FEFF496BEEE:FG=1; BAIDUID_BFESS=56E7AD86AA3B7C032C167FEFF496BEEE:FG=1; ZFY=O0PLDpLNwXmDMBTHglu04UoHbGpcqGRg4Dc:B3Lt3FLo:C; BAIDU_WISE_UID=wapp_1709522676567_590; H_WISE_SIDS=40210_40206_40215_40222_40061_40295_40290_40288_40286_40318_40320_40079_40364_40351; PSINO=7; delPer=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[A24tJn4Wkd_]=mk3SLVN4HKm; H_PS_PSSID=40210_40206_40215_40222_40061_40295_40290_40288_40286_40318_40320_40079_40364_40351_40369_40377; BCLID=8593173654593079238; BCLID_BFESS=8593173654593079238; BDSFRCVID=BMKOJeC62ljYkWTqg5HeriDsoTPGABoTH6_nWdHAEyCEMAuZ_zqtEG0PYM8g0KuhoX2AogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; BDSFRCVID_BFESS=BMKOJeC62ljYkWTqg5HeriDsoTPGABoTH6_nWdHAEyCEMAuZ_zqtEG0PYM8g0KuhoX2AogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF=JRujoDtKtKD3eb4kh45Shn-QqxbXqMjuW2OZ0l8KtJR8oJv53bQJjfk8KxrRb-RnLgvC5J7mWIQrDx3gyMQp2ftkXtQtXqRE-6n4KKJxylCWeIJo5t7oW5DFhUJiBbFHBan7VlbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtPPhbRO4-TFhDTO0jMK; H_BDCLCKID_SF_BFESS=JRujoDtKtKD3eb4kh45Shn-QqxbXqMjuW2OZ0l8KtJR8oJv53bQJjfk8KxrRb-RnLgvC5J7mWIQrDx3gyMQp2ftkXtQtXqRE-6n4KKJxylCWeIJo5t7oW5DFhUJiBbFHBan7VlbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtPPhbRO4-TFhDTO0jMK; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1709522676,1709631465,1709713151; USER_JUMP=-1; st_key_id=17; video_bubble0=1; tb_as_data=3362df7a558a4ac2b8a3c9d536418cebc8c2674beb8a4678363df771f451f0bbe1a970f35124041ee296e27cf2ee449d01fc639c46add7b19b8ca68de9759124587c34abbbbef13e6d0a90834dd8dede860f9bafa00544aae89dc6f46f23ef545a863075af86597321e19a6828a6c7ac; arialoadData=false; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1709732915; XFI=3ac2e900-dbc0-11ee-9aaf-73222c87f3e7; BA_HECTOR=2k80ah24aha10h8hakalah856namkm1iugt1k1t; ab_sr=1.0.1_ZDBlYTU1NTVlNDdhZmQ0OTA2ODg3ZWU4YzEyNTJkNDMwODU1OTdkYjNjMzgxMzA4ODY5ZGM2NWU5YWZiYjVhOTFjYWFmMTkxMDMyYTM5OGY5NzljYTljZDg3ODYzMWYzODBlODE0NTZiMjk5NGRhNmNhMjJhZDNmZGM2MjNmYzE1ZWZlYzM3MTBhMjlmZTM5MzA0ODQ5NDIyODliZjU0Mg==; st_data=ccf291362f3d497ad9e3445cb2dd65e37c8b37bf6eb94b62319f5aec7db02751d5f3212ccbed7aa123846b6d5b4352c2022d62689083b0c9379f01398319071f2dc19498de025a7658210b1a067a748117dc19233fb39c6cd40f6696fc1d6c5249da126ab5dd7ce35f3b3047ab33fa6212348e9d24df35fc0f9f42089bc474532d0cb612d40424b749074bd9a8702745; st_sign=354918f7; XFCS=EC98CBE09F96B89CC004B737A64D4E256208CD64957E600F41EC94D6FA4EFAEF; XFT=PG/N53D+Xrox45URbthUMFzZgl/1o4M8hANuTCUcu04=; RT="z=1&dm=baidu.com&si=c31848c6-a52a-4341-b0c5-d6955c194c96&ss=ltfj2nq4&sl=p&tt=t5y&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=2baynwak&cl=brdcx&ld=brg1m&ul=brjfx"'
        }
        self.filepath = file_path + file_path_file + '/' + addr

    def send_request(self, params):
        res = requests.get(self.url, headers=self.headers, params=params)
        time.sleep(3)
        return res.text

    def save_file(self, page, word, con):
        # print(self.filepath + '_' + word + '_' + str(page) + '.html')
        with open(self.filepath + '_' + word + '_' + str(page) + '.html', 'w', encoding='utf-8') as f:
            f.write(con)

        print(f'Save page {page} done')

    def run(self):
        word = input('Please input a word to start download files from tieba: ')
        pages = int(input('Please input page number: '))

        for page in range(pages):
            params = {
                'kw': word,
                'pn': page * 50
            }

            data = self.send_request(params)
            self.save_file(page, word, data)


if __name__ == "__main__":
    te = Tieba()
    te.run()

    ## already been prevented.
