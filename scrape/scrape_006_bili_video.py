# 提取bilibili单页视频

# 找到包含所有视频的url
# 解析出响应里的url, 20
# 对这些url 发送请求， 获取单个视频页面的响应内容
# 从响应内容里提取对应的视频url
# 对视频url 发送请求
# 保存请求到的视频内容

import requests
from fake_useragent import UserAgent
from lxml import etree
import re
from retrying import retry
import os
import time

headers = {
    'User-Agent': UserAgent().random,
    'Referer': 'https://www.bilibili.com/v/music/?spm_id_from=333.1007.0.0',
    'Cookie': "buvid3=34877BFC-F291-D786-8F69-2CDA7B7290F358719infoc; b_nut=1709864358; i-wanna-go-back=-1; b_ut=7; _uuid=BBFBC985-5B3C-2FC2-ECAE-C79B9C8AF56958996infoc; enable_web_push=DISABLE; FEED_LIVE_VERSION=V8; header_theme_version=undefined; home_feed_column=5; browser_resolution=1536-703; buvid4=95C04B34-CA04-3DC7-C5E5-C76EB199BF9959427-024030802-N1mGaPJ/77MvC0IVYkEH7Q%3D%3D; buvid_fp=ead5b84653cc9da8375a37773abaee6b; CURRENT_FNVAL=4048; is-2022-channel=1; rpdid=|(J~J|RlR)l)0J'u~|m)YRJm|; PVID=1; SESSDATA=9023a09b%2C1725416595%2C33dad%2A32CjBovAwZf-sAihQddmUYDFxNVHs5AEjLpqfXm38eBzkOPWZnIJj0lFmR_ibBKcfr5lISVjZCdG8xYUpiN1RlZS02MVNFd1JyY19tbUNnMk5ZQjM1R0pFdXBRcHlDcTBxTW9aamtsRi0yZGpIUUE4OXloM1I4X2U3c0Y2Yk5fRUNEeG5FZXItcWpBIIEC; bili_jct=a8f7df8fb6da72ca77537a13b9ce5e39; DedeUserID=221041590; DedeUserID__ckMd5=259ac74fa80b69f7; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTAxNDM1NDAsImlhdCI6MTcwOTg4NDI4MCwicGx0IjotMX0.nTnTI5n_epEjiGhfYH-YMBHLdlEgfE1TZm1n7487BFY; bili_ticket_expires=1710143480; bp_video_offset_221041590=906460587379130582; b_lsid=36264E18_18E218ACA4F; sid=7n6baao3"
}

# page_url = 'https://search.bilibili.com/all?keyword=%E5%94%AF%E7%BE%8E%E9%9F%B3%E4%B9%90&from_source=webtop_search&spm_id_from=333.1073&search_source=5'
page_url = 'https://search.bilibili.com/all?keyword=%E5%94%AF%E7%BE%8E%E9%9F%B3%E4%B9%90'


class DownloadVideo:
    def __init__(self):
        pass

    def send_req(self, url):
        return requests.get(url, headers=headers)

    def sortout_urls(self, url):
        pass
        con = self.send_req(url).text
        # print(con)
        tcp = 'https:'
        video_infos = []

        html = etree.HTML(con)
        urls = html.xpath('//*[@class="bili-video-card"]/div[2]/div/div/a/@href')
        titles = html.xpath('//*[@class="bili-video-card"]/div[2]/div/div/a/h3/@title')

        id = 1

        for each in list(zip(urls, titles)):
            url = f'https:{each[0]}'
            title = ''.join(filter(str.isalnum, each[1]))[:20]
            print(url)
            self.save_indiv_video(url, title, id)
            id = id + 1

            if id == 2:
                break

        # //  bili link = https://search.bilibili.com/all?vt=86364257&keyword=%E5%94%AF%E7%BE%8E%E9%9F%B3%E4%B9%90
        # 唯美音乐: https://search.bilibili.com/all?keyword=%E5%94%AF%E7%BE%8E%E9%9F%B3%E4%B9%90&from_source=webtop_search&spm_id_from=333.1073&search_source=5

    # // 拿到url, 发送请求

    def save_to_file(self, ad, vd, title):

        self.write_to_file(self.send_req(ad).content, "audio", title)
        self.write_to_file(self.send_req(vd).content, "video", title)
        pass

    def write_to_file(self, con, t, title):

        with open(f'../../download/videos_002/{t}s/{title}_{t}.mp4', 'wb') as f:
            f.write(con)

    def combine_video(self, title, id):

        _file_path = 'D:/Program/programme/download/videos_002/'
        _ad_file_path = _file_path + f'audios/{title}_audio.mp4'
        _vd_file_path = _file_path + f'videos/{title}_video.mp4'

        _t = [_ad_file_path, _vd_file_path]

        _concat_file_path = _file_path + f'_video_txt/{title}.txt'
        # print(_t)

        for i in range(len(_t)):
            print(_t[i])

            with open(_concat_file_path, 'a+', encoding='utf-8') as f:
                _v_file = f"file '{_t[i]}' \n"
                f.write(_v_file)

        _result_file_path = _file_path + f'combined_videos/{title}.mp4'
        print(_result_file_path)

        _cmd = f'ffmpeg -f concat safe 0 -i {_concat_file_path} -c copy {_result_file_path}'

        print(_cmd)
        os.popen(_cmd)
        pass

    def save_indiv_video(self, url, title, id):
        # //from page to get audio and video url to get the original content.
        urls = self.get_v_url(url)

        self.save_to_file(urls['ad'], urls['vd'], title)
        print(f"Video {title} download complete. {id}")

        self.combine_video(title, id)

    def get_v_url(self, url):
        # return audio and video url
        con = self.send_req(url).text
        # // audio and video type on b site
        # Audio : 30280  纯音乐  30232  30216
        # Video : 30032  纯视频  30016
        # get audio url
        get_ad = re.findall(r'"id":30280,"baseUrl":"(.*?)","base_url"', con)
        if len(get_ad) == 0:
            get_ad = re.findall(r'"id":30232,"baseUrl":"(.*?)","base_url"', con)
        if len(get_ad) == 0:
            get_ad = re.findall(r'"id":30216,"baseUrl":"(.*?)","base_url"', con)

        # print(get_ad[0])
        # get video url
        get_vd = re.findall(r'"id":32,"baseUrl":"(.*?)","base_url"', con)
        if len(get_vd) == 0:
            get_vd = re.findall(r'"id":16,"baseUrl":"(.*?)","base_url"', con)

        # print(get_vd[0])

        return {'ad': get_ad[0], 'vd': get_vd[0]}

    def run(self, url):
        self.sortout_urls(url)


if __name__ == '__main__':
    print('---------Start...')
    dl = DownloadVideo()
    dl.run(page_url)
    print('---------End...')
