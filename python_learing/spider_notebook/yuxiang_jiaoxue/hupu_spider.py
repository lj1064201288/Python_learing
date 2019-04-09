'''
爬取虎扑论坛篮球场论坛
需要获取的信息是标题,链接,作者,发布时间,回复数,浏览数,最后回复时间,最后回复人
url:https://bbs.hupu.com/nba
'''

import requests, random, time
from lxml import etree
from Mongodb_Sql import Mongo_DB

agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]


def get_url(url):
    '''
    接收需要爬取的URL进行请求
    :param url: 需要爬取的网页
    :return: 返回源代码
    '''

    headers = {
        'User-Agent': random.choice(agents)
    }
    try:
        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            html = res.text
            return html

    except Exception as e:
        print(e.args)

def parse_datas(url):
    '''
    分析网页数据,得到需要的信息
    :param url:
    :return:
    '''
    html = get_url(url)
    if html:
        html = etree.HTML(html)
        # 得到需要获取的数据的节点
        items = html.xpath('//ul[@class="for-list"]/li')
        for item in items:
            # 获取标题
            title = item.xpath('string(./div/a[@class="truetit"])')
            # 获取链接
            href = 'https://bbs.hupu.com' + item.xpath('./div[@class="titlelink box"]/a[@class="truetit"]/@href')[0]
            # 作者名字
            author = item.xpath('./div[@class="author box"]/a/text()')[0]
            # 发布时间
            release_time = item.xpath('./div[@class="author box"]/a/text()')[1]
            # 回复数量
            reply_num = item.xpath('./span[@class="ansour box"]/text()')[0].split('/')[0]
            # 浏览数量
            brower_num = item.xpath('./span[@class="ansour box"]/text()')[0].split('/')[1]
            # 最后回复时间
            last_reply = item.xpath('./div[@class="endreply box"]/a/text()')[0]
            # 最后回复的人
            last_people = item.xpath('./div[@class="endreply box"]/span/text()')[0]
            # 将需要的数据保存到一个字典当中
            datas = {
                'title': title,
                'href': href,
                'author': author,
                'relase_time': release_time,
                'reply_num': reply_num,
                'brower_num': brower_num,
                'last_repiy': last_reply,
                'last_people': last_people
            }
            save_datas(datas)

def save_datas(datas):
    '''
    保存数据到mongodb数据库
    :param datas:
    :return:
    '''
    print(datas)
    db = Mongo_DB('hupu', 'NBA')
    db.open_data()
    db.insert_data(datas)
    db.close_data()

def main():
    '''
    主函数:执行程序的开关
    :return: None
    '''
    urls = ["https://bbs.hupu.com/nba-{}".format(i) for i in range(1,6)]
    for url in urls:
        parse_datas(url)

if __name__ == '__main__':
   main()


