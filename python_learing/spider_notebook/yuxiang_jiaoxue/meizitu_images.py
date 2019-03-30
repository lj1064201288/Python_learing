import os, time
import random
import requests
from lxml import etree

# agent列表
agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]

# 获取页面
def get_spider(url):
    '''

    :param url: 接收的网页地址
    :param headers: 网页头部信息
    :return: 返回网页数据
    '''

    try:
        # 访问得到的url
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
    except Exception as e:
        print(e.args)

# 爬取妹子图的第二段链接
def mz_spider(url):
    '''
    获取到妹子图页面的图片,返回链接
    :param url: 需要爬取的页面
    :param headers: 网页的头部信息
    :return: 返回第二段链接
    '''
    # 将得到的地址发送给函数获取网页的信息
    html = get_spider(url)
    data = etree.HTML(html)
    # 找到图片第二段的链接
    img_src = data.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        twomz_spider(img_url)

# 获取第二链接页面的图片链接
def twomz_spider(url):
    '''
    :param url: 需要爬取的网站
    :return: 需要下载的图片
    '''
    res = get_spider(url)
    html = etree.HTML(res)
    # 获取标题
    title = html.xpath('//div[@class="content"]/h2/text()')[0]
    # 获取图片的数量
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')
    for i in range(1, int(page_num[-2])+1):
        img_scr = url + '/' + str(i)
        download_img(img_scr, title)

# 下载图片
def download_img(url, title):
    '''
    下载图片保存
    :param url: 图片的页面
    :param title: 图片的标题
    :return:
    '''
    res = get_spider(url)
    html = etree.HTML(res)
    href = html.xpath('//div/p/a/img/@src')[0]
    images = requests.get(href, headers=headers)
    # 图片保存的地址
    root_dir = '../datas/images/mztu' + '/' + title
    img = href.split('/')[-1]
    # 判断路径是否存在
    if not  os.path.exists(root_dir):
        os.makedirs(root_dir)
    # 存储图片
    with open(root_dir + '/' + img, 'wb') as f:
        f.write(images.content)
        f.close()
        print(title + img + ' 下载成功')


# 主函数
if __name__ == '__main__':

    headers = {
        'Referer': 'https://www.mzitu.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': random.choice(agents)
    }

    for i in range(1,200):
        url = 'https://www.mzitu.com/page/{}/'.format(i)
        mz_spider(url)


