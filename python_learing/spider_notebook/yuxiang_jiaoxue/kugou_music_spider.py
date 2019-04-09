'''
项目分析:
    - 1.获取到酷狗排行榜top前200的歌曲,需要得到名称,歌手,歌曲时间, 排名
    - 2.将获取到的信息保存mongodb输出库当中
'''

import random
import requests
from Mongodb_Sql import Mongo_DB
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
    'User-Agent': random.choice(agents),
    'upgrade-insecure-requests': '1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}


Mongo_DB = Mongo_DB('kg_music', 'rank')

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

            # 获取排名信息
            ranks = soup.select('.pc_temp_num')
            # 获取歌手与歌曲名称信息
            singers = soup.select('.pc_temp_songname')
            # 获取歌曲时间信息
            song_times = soup.select('.pc_temp_time')
            for rank, singer, times in zip(ranks, singers, song_times):
                rank = rank.get_text().strip()
                singer_name = singer.get('title').split('-')[0]
                song_name = singer.get('title').split('-')[1]
                song_time = times.string.strip()
                items = {
                    'rank':rank,
                    'singer_name':singer_name,
                    'song_name':song_name,
                    'song_time':song_time
                }
                print(items)
                Mongo_DB.open_data()
                Mongo_DB.insert_data(items)
                Mongo_DB.close_data()

    except Exception as e:
        print(e.args)




if __name__ == "__main__":
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(i) for i in range(1,24)]

    for url in urls:
        kg_spider(url)
