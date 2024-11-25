import json
import time
import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

# connect db

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '28340186',
    'db': 'wangbi01'
}

# create connection
# conn = pymysql.connect(**db_config)
# cur = conn.cursor()
# # print(cur)
# sql = 'select * from tb'
#
# # receive how many data
# res = cur.execute(sql)
# print(res)
# print(cur.fetchall())  # 从游标对象拿所有数据
#
# cur.close()
# conn.close()


class ScrapeDouBanM250:
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?'
        self.headers = {
            'User-Agent': UserAgent().random
        }

    def sendrequest(self, page):
        res = requests.get(self.url + f'start={page}', headers=self.headers)
        print(self.url + f'?start={page}')
        return res.text

    @staticmethod
    def parseres(text):
        html = etree.HTML(text)
        name = html.xpath('//div[@class="hd"]/a/span[1]/text()')
        score = html.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/div/span[2]/text()')

        return dict(zip(name, score))

    def savedata(self, data, name):
        with open(f'../../download/files/{name}.txt', 'w') as f:
            f.write(str(data))

    def savetodb(self, id, title, rate):

        conn = pymysql.connect(**db_config)
        cur = conn.cursor()
        cur.execute(f'insert into douban values("{id}", "{title}", "{rate}")')
        conn.commit()

        cur.close()
        conn.close()

    def run(self, name):
        result = []

        for i in range(0, 250, 25):
            text = self.sendrequest(i)
            # self.parseres(text)
            result.append(self.parseres(text))
            time.sleep(1)

        # return result
        # self.savedata(result, name)

        id = 0

        for i in range(len(result)):
            for key, value in result[i].items():
                self.savetodb(id, key, value)
                id = id + 1

        print(f'Save to db done, total {id} pieces.')


if __name__ == "__main__":
    # print('Start....')
    cdb = ScrapeDouBanM250()
    cdb.run("DouBanMovie250")
    print('End....')
