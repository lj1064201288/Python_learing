'''
获取全国公园信息保存至MySQL数据库当中
地点检索详情链接
http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求
基础地址
http://api.map.baidu.com/place/v2/search?
参数
    query:公园
    region: 成都市
    scope: 2
    page_size: 20
    output:json
    ak:TLkSqB53Mwap6mRvNiHbNBkL7HiGmwcu
'''

import requests
from lxml import etree
from Mysql_API import Mysql_API

# 百度地图API
def get_json(loc, page_num=0):
    '''
    :param loc: 城市地址
    :param page_num: 页数
    :return:
    '''
    data = {
        'query':'公园',
        'region': loc,
        'scope': '2',
        'page_size':20,
        'page_num': page_num,
        'output': 'json',
        'ak':'futZzaYuiPwbInIcjA9vTLwlnkoGuTg5'
    }

    url = "http://api.map.baidu.com/place/v2/search?"
    res = requests.get(url, params=data, headers=headers)
     # print(res.url)
    decodejson = res.json()
    # page_num += 1

    return decodejson

# 获取中国省份列表
def province_spider():
    url = "http://www.tcmap.com.cn/list/jiancheng_list.html"
    res = requests.get(url)
    response = res.content.decode('GB2312')
    # print(response)
    html = etree.HTML(response)
    provinces = html.xpath('//tr/td/a/text()')
    return  provinces

# 提取信息
def parse_data(data):
    # 增加判定信息
    if data['name']:
        name = data['name']
    else:
        name = None
    if 'location' in data.keys():
        if data['location']['lat']:
            global  lat
            lat = data['location']['lat']
        else:
            lat = None
        if data['location']['lng']:
            global lng
            lng = data['location']['lng']
        else:
            lng = None
    if 'address' in data:
        address = data['address']
    else:
        address = None
    if 'area' in data:
        area = data['area']
    else:
        area = None
    if 'uid' in data:
        uid = data['uid']
    else:
        uid = None
    if 'city' in data:
        city = data['city']
    else:
        city = None

    items = {
        'name': name,
        'locatlat':lat,
        'locatlng': lng,
        'address': address,
        'area': area,
        'uid': uid,
        'city': city
    }
    # print(items)
    yield items

# 提取所有市区
def city_spider(citys):
    for city in citys['results']:
        datas = get_json(city['name'])
        for data in datas['results']:
            items = parse_data(data)
            down_sql(items)

def down_sql(items):
    sql = Mysql_API()
    for item in items:
        try:
            print(item)
            sql.insert_data('park', 'park', item)
        except Exception as e:
            print(e.args)

# 启动函数
def main():

    province_list = province_spider()
    municipality = ['北京', '天津', '上海', '重庆', '香港特别行政区', '澳门', '台湾', ]
    # print(province_list)
    for province in province_list:
        if province in municipality:
            municipality_datas = get_json(province)['results']
            for municipality_data in municipality_datas:
                items = parse_data(municipality_data)
                down_sql(items)
        else:
            citys = get_json(province)
            city_spider(citys)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    # 爬取的页数统计
    global page_num
    main()

