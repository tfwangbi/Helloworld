import re

import requests
from fake_useragent import UserAgent
from moviepy.editor import *

voice_url = 'https://xy61x159x92x162xy.mcdn.bilivideo.cn:4483/upgcxcode/40/99/1445099940/1445099940-1-30232.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709872364&gen=playurlv2&os=mcdn&oi=3730454858&trid=0000c90c08e4b4cb4be88a491b89eeddc6efu&mid=221041590&platform=pc&upsig=7c39591a7a2ab03c31fafebcdcdf8dbc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003214&bvc=vod&nettype=0&orderid=0,3&buvid=34877BFC-F291-D786-8F69-2CDA7B7290F358719infoc&build=0&f=u_0_0&agrr=0&bw=13086&logo=A0000001'
video_url = 'https://xy61x159x92x162xy.mcdn.bilivideo.cn:4483/upgcxcode/40/99/1445099940/1445099940-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709872364&gen=playurlv2&os=mcdn&oi=3730454858&trid=0000c90c08e4b4cb4be88a491b89eeddc6efu&mid=221041590&platform=pc&upsig=2be50865d383dddfefa277dc9a5a1e74&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003214&bvc=vod&nettype=0&orderid=0,3&buvid=34877BFC-F291-D786-8F69-2CDA7B7290F358719infoc&build=0&f=u_0_0&agrr=0&bw=306583&logo=A0000001'

url = 'https://xy61x159x92x162xy.mcdn.bilivideo.cn:4483/upgcxcode/40/99/1445099940/1445099940-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1709874990&gen=playurlv2&os=mcdn&oi=3730454858&trid=0000ca8bd0faadf047a687d882446db78b56u&mid=0&platform=pc&upsig=461449b6c62d7730e695527aa6a84c67&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1003214&bvc=vod&nettype=0&orderid=0,3&buvid=&build=0&f=u_0_0&agrr=0&bw=24382&logo=A0000001'
# Audio : 30280  纯音乐
# Video : 30032  纯视频

# headers = {
#     'User-Agent': UserAgent().random,
#     'Referer': 'https://www.bilibili.com/video/BV13A4m1G7v2/?spm_id_from=333.1073.channel.secondary_floor_video.click'
# }
#
# res = requests.get(url, headers=headers)
#
# # print(res.content)
#
# with open('../../download/videos_001/douban_test.mp4', 'wb') as f:
#     f.write(res.content)
#
# print('done')


# 1445099940/1445099940-1-30080.m4s

bi_url = 'https://www.bilibili.com/video/BV13A4m1G7v2/?spm_id_from=333.1073.channel.secondary_floor_video.click&vd_source=a547ccdf98f8a2709d1adc32aa94b5cc'
headers = {
    'User-Agent': UserAgent().random,
    'Referer': 'https://www.bilibili.com/v/music/?spm_id_from=333.1007.0.0'
}

# 1st round reqyest
res2 = requests.get(bi_url, headers=headers)

# print(res2.text)

# get audio url
get_ad = re.findall(r'"id":30280,"baseUrl":"(.*?)","base_url"', res2.text)
print(get_ad[0])
# get video url
get_vd = re.findall(r'"id":32,"baseUrl":"(.*?)","base_url"', res2.text)
print(get_vd[0])

# 2nd round request to get video and audio

headers2 = {
}

res_ad = requests.get(get_ad[0], headers=headers)
res_vd = requests.get(get_vd[0], headers=headers)

with open('../../download/videos_001/douban_ad.mp4', 'wb') as f:
    f.write(res_ad.content)

with open('../../download/videos_001/douban_vd.mp4', 'wb') as f:
    f.write(res_vd.content)

print("done")


# 合成视频

def clip_video(ad, vd):
    vd = VideoFileClip(vd)
    ad = AudioFileClip(ad)
    vd_temp = vd.set_audio(ad)
    vd_temp.write_videofile('../../download/videos_001/douban_001.mp4')


if __name__ == "__main__":
    ad = '../../download/videos_001/douban_ad.mp4'
    vd = '../../download/videos_001/douban_vd.mp4'
    clip_video(ad, vd)

    print("Combined done")
