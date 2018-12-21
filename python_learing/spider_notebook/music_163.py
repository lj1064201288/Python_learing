import requests
from lxml import etree

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'music.163.com',
    'Referer':'https://music.163.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

url = "https://music.163.com/discover/toplist?id=3779629"
response = requests.get(url, headers=headers, allow_redirects=False)
iframe = response.text
print(iframe)
html = etree.HTML(iframe)
contents = html.xpath('//tbody/tr')

for content in contents:
    name = content.xpath('./td/div/div/div/span/a/b/@title')[0].replace(' ', '')
    music_id = content.xpath('./td/div/div/span/@data-res-id')[0].strip()
    print(name, music_id)
