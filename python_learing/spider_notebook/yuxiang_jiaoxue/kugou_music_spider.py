'''
项目分析:
    - 1.获取到酷狗排行榜top前200的歌曲,需要得到名称,歌手,歌曲时间, 排名
    - 2.将获取到的信息保存mongodb输出库当中
'''

import random
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup

agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]


headers = {
    'User-Agent': random.choice(agents)
}

# 爬去酷狗top500的歌曲信息
def kg_spider(url):
    '''
    爬去酷狗音乐的方法
    :param url: 请求地址
    :return:
    '''
    res = requests.get(url, headers=headers)
    try:
        if res.status_code == 200:
            html = res.text
            soup = BeautifulSoup(html, 'lxml')
            rank = soup.select('.pc_temp_num')
            title = soup.select('.pc_temp_songname')
            songer_time = soup.select('.pc_temp_time')
            ranks = []
            titles = []
            songer_times = []
            for r in rank:
                d = r.get_text().strip()
                ranks.append(d)
            for t in title:
                b = t.get_text().replace(' ', '')
                titles.append(b)
            for s in songer_time:
                a = s.get_text().strip()
                songer_times.append(a)
            datas = zip(ranks, titles, songer_times)
            print(datas)
            items = []
            for data in datas:
                items.append(data)

            print(items)
            # ranks.append(r.get_text().strip() for r in rank)
            # print(list(ranks))
    except Exception as e:
        print(e.args)




if __name__ == "__main__":
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(i) for i in range(1,24)]

    for url in urls:
        kg_spider(url)
        break