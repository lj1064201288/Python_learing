'''
爬取网易云音乐歌手以及歌手的id信息
class:u-cover u-cover-5
class:nm nm-icn f-thide s-fc0
'''
import requests, csv, random
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

def get_artlist(url):
    headers = {
        'User-agent': random.choice(agents),
        'Host': 'music.163.com',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://music.163.com/',
        'Upgrade-Insecure-Requests': '1'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    html = response.text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # 数据存储路径
    root_dir = open('../datas/tables/music163.csv', 'a')
    file = csv.writer(root_dir)
    title = ['id', 'singer']
    file.writerow(title)
    # 获取需要的数据(id, songer)
    items = soup.find_all('a', attrs={"class":'nm nm-icn f-thide s-fc0'})
    for item in items:
        singer = item.string
        singer_id = item['href'].split('=')[-1]
        datas = (singer_id, singer)
        print(datas)
        file.writerow(datas)



if __name__ == '__main__':

    # id列表
    id_list = [1001, 1002, 1003, 2001,2002,2003, 6001,6002,6003, 7001,7002,7003, 4001,4002,4003]
    # 字母列表
    queue_list = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]



    for i in id_list:
        for j in queue_list:
            url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(i, j)
            get_artlist(url)

