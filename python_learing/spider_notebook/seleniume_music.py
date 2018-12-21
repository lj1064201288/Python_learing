from selenium import webdriver
from lxml import etree

url = "https://music.163.com/discover/toplist?id=3779629"

option = webdriver.ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=option)
browser.get(url)
browser.switch_to_frame('contentFrame')
iframe = browser.page_source
print(iframe)
html = etree.HTML(iframe)
contents = html.xpath('//tbody/tr')

for content in contents:
    name = content.xpath('./td/div/div/div/span/a/b/@title')[0].replace(' ', '')
    music_id = content.xpath('./td/div/div/span/@data-res-id')[0].strip()
    print(name, music_id)