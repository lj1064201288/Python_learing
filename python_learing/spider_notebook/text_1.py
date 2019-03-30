import requests
from lxml import etree

url = 'https://www.baidu.com'

response = requests.get(url)
html = response.text
print(html)
a = etree.HTML(html)
b = a.xpath('//div[@class="s_tab"]/@class')
print(b)