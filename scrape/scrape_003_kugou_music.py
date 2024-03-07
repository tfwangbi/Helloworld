import requests
import time


#Music information url:

info_url = 'https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1709644502743&mid=7e27cb206f90350205ba4659f37e1511&uuid=7e27cb206f90350205ba4659f37e1511&dfid=3exvPB07ffH80LF6Qh1PqSqu&appid=1014&platid=4&encode_album_audio_id=a1i11612&token=&userid=0&signature=b71221cc2f4041a3b2abadff97ef3d69'

# Music url
# url = 'https://www.kugou.com/yy/html/rank.html'
m_url = 'https://webfs.hw.kugou.com/202403052055/9b6331ede6df5d98385186a19d1df409/KGTX/CLTX001/9d088da53d9d17eb96e4d1dd2f5c6714.mp3'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

m_response = requests.get(m_url, headers=headers).content

m_offset = "music_"

with open('../../download/music_001/{}.mp3'.format(m_offset), 'wb') as f:
    f.write(m_response)

    print('Music download done.')

