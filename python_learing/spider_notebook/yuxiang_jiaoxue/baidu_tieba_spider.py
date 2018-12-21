'''
使用爬虫编写一个可以输入搜索内容之后得到搜索的贴吧信息的爬虫,然后可以使用json格式进行保存
'''
import json
import time
import random
from bs4 import BeautifulSoup
from urllib import parse, request

user_agents = [
    'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
    'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
]


def execute_fun(kw, pn):
    base_url = "https://tieba.baidu.com/f?"

    headers = {
        'User-Agent': random.choice(user_agents)
    }

    data = {
        'kw': kw,
        'ie': 'utf-8',
        'pn': pn
    }
    data = parse.urlencode(data)
    url = base_url + data
    req = request.Request(url, headers=headers)
    print(req, url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        items = parse_html(html)
        write_infos(items)
    except Exception as e:
        print(e.args)

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', attrs={'class':' j_thread_list clearfix'})
    for li in lis:
        items = {}
        title = li.find(class_='j_th_tit ')
        items['标题'] = title.string
        href = 'https://tieba.baidu.com' + li.find('a').attrs['href']
        items['链接'] = href
        comment = li.find('span', attrs={'class':'threadlist_rep_num center_text'})
        items['评论次数'] = comment.string
        author = li.find('a', attrs={'class':'frs-author-name j_user_card '})
        if author:
            items['作者'] = author.string

        yield items

def write_infos(items):
    path = open(r'../datas/tables/' + kw + '.json', 'a', encoding='utf-8')
    for item in items:
        content = json.dumps(dict(item))
        path.write(content + '\n')
    path.close()



if __name__ == '__main__':
    kw = input('请输入要搜索的贴吧:')
    num = input('请输入要爬去的页数:')
    page = [pn*50 for pn in range(int(num))]
    for pn in page:
        execute_fun(kw, pn)
        time.sleep(2)
