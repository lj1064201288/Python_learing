import random, json
from lxml import etree
from urllib import request

agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]

def get_html():
    '''
    对页面进行爬取,获取html
    :param url: 需要爬取的URL
    :return:
    '''


    agent = random.choice(agents)
    headers = {
        'User-Agent':agent
    }

    req = request.Request(url, headers=headers)
    try:
        response = request.urlopen(req)
        if response.status == 200:
            print('请求成功...')
            html = response.read().decode('utf-8')
            return html
    except Exception as e:
        print('请求失败', e.args)

def parse_html():
    '''
    解析页面信息
    :param html:页面信息
    :return: 得到的数据
    '''
    content = etree.HTML(get_html())
    trs = content.xpath('//tbody/tr')

    for tr in trs:
        item = {}
        school = tr.xpath('./td[2]/div/text()')[0]
        ranking = tr.xpath('td[1]/text()')[0]
        local = tr.xpath('td[3]/text()')[0]
        total = tr.xpath('td[4]/text()')[0]
        index_score = tr.xpath('td[5]/text()')[0]
        item['ranking'] = ranking
        item['school'] = school
        item['local'] = local
        item['total'] = total
        item['index_score'] = index_score
        yield item

def write_json():
    items = parse_html()
    path = open(r'../datas/tables/' + str(year) + '.json', 'a', encoding='utf-8')
    for item in items:
        path.write(json.dumps(item, ensure_ascii=False) + '\n')
    path.close()


if __name__ == '__main__':
    years = ['2016', '2017', '2018']
    for year in years:
        url = 'http://zuihaodaxue.com/zuihaodaxuepaiming{0}.html'.format(year)
        get_html()
        write_json()
