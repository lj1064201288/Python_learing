from urllib import request
import os, requests, random
from lxml import etree

def Schedule(blocknum, blocksize, totalsize):
    '''
    显示下载的进度
    :param blocknum: 已经下载的数据快
    :param blocksize: 数据块的大小
    :param totalsize: 文件的大小
    :return:
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per > 100:
        per = 100
    print('当前下载进度为:{}'.format(per))


user_agent = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]

headers = {
    'User-Agent': random.choice(user_agent)
}

url = 'http://www.ivsky.com/tupian/ziranfengguang/'

response = requests.get(url, headers=headers)
# print(response.text)
html = etree.HTML(response.text)
img_urls = html.xpath('//div[@class="il_img"]/a/img/@src')
for img_url in img_urls:
    root_dir = '../datas/images/tiantang'
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_url.split('/')[-1]
    request.urlretrieve('http:'+img_url, root_dir+'/'+filename, Schedule)