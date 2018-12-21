import os, random, json, time
from urllib import parse, request

# queryWord: 壁纸
# word: 壁纸
# pn: 120
# rn: 30
# gsm: 78
# https://image.baidu.com/search/index?tn=baiduimage&word=%E5%A3%81%E7%BA%B8&pn=90

agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]

def Schedule(blocknum, blocksize, totalsize):
    '''
    显示下载进度
    :param blocknum: 已经下载的数据快
    :param blocksize: 数据块的大小
    :param totalsize: 远程文件大小
    :return:
    '''
    per = 100.0 * blocknum * blocksize/totalsize
    if per > 100:
        per = 100
    print('当前下载进度为:{}'.format(per))

def get_json(key, page):

    base_url = 'https://image.baidu.com/search/acjson?'
    agent = random.choice(agents)

    headers = {
        'User-Agent':agent
    }

    data = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'pn': str(page),
        'word': key,
    }

    url = base_url + parse.urlencode(data)
    print(url)
    req = request.Request(url, headers=headers)
    try:
        response = request.urlopen(req)
        if response.status == 200:
            print('请求成功...')
            html = response.read().decode()
            parse_html(html)
    except Exception as e:
        print('请求失败...', e.args)

def parse_html(html):
    datas =json.loads(html).get('data')
    for data in datas[:-1]:
        title = data.get('fromPageTitleEnc')
        imageurl = data.get('thumbURL')
        download_image(title, imageurl)

def download_image(title, imageurl):
    path = r'../datas/images/' + key
    if not os.path.exists(path):
        os.makedirs(path)
    request.urlretrieve(imageurl, path + os.sep + title + '.jpg', Schedule)
    print('下载{0}成功...'.format(title))


if __name__ == '__main__':
    key = input('请输入你要下载的图片类型:')

    pages = [page*30 for page in range(11)]

    for page in pages:
        get_json(key,page)
        time.sleep(1)
