import requests, random
from bs4 import BeautifulSoup

# User-Agent列表
agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]

# 访问需爬取的网站
def get_cnblogs(url):
    '''
    :param url: 访问的地址
    :return: 反馈的数据
    '''

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            parse_cnblogs(html)
    except Exception as e:
        print('请求失败!', e.args)

# 解析页面信息,得到需要的数据
def parse_cnblogs(html):
    '''

    :param html: 网页源码
    :return: 返回需要的数据
    '''
    # 保存输出的字典
    items = []
    soup = BeautifulSoup(html, 'lxml')
    # 获取标题
    titles = soup.select('div[class="post_item_body"] h3 a')
    # 获取作者名称
    authors = soup.select('div[class="post_item_foot"] a[class="lightblue"]')
    # 获取作者首页链接
    authors_links = soup.select('div[class="post_item_foot"] a')
    # 获取文章发布的时间
    issue_time = soup.select('div[class="post_item_foot"]')



if __name__ == '__main__':
    # 需要爬取的网页
    url = 'https://www.cnblogs.com/cate/python/#p{}'
    # 构建headers头部信息
    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9',
        'upgrade-insecure-requests': '1',
        'user-agent': random.choice(agents)
    }

    page = int(input('请输出你要获取的页数:'))
    for i in range(1, page+1):
        get_cnblogs(url.format(i))
        break