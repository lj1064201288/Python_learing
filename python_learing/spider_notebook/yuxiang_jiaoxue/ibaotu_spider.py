'''
爬取爱包图视频
url:https://ibaotu.com/shipin/7-0-0-0-0-1.html
'''

import requests
from lxml import etree

class Ibaotu_Spider(object):
    def __init__(self):
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_spider(self, url):
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                self.parse_spider(res.text)
        except Exception as e:
            print(e.args)

    def parse_spider(self, html):
        html = etree.HTML(html)
        src = html.xpath('//div[@class="video-play"]/video/@src')
        title = html.xpath('//a[@class="shade-box"]/span/text()')
        for src, title in zip(src, title):
            self.write_vedio(src, title)

        next_page = html.xpath('//a[@class="next"]/@href')
        if next_page:
            next_url = 'https:' + next_page[0]
            print(next_url)
            self.get_spider(next_url)
        else:
            print('已经爬取完毕,谢谢使用!')


    def write_vedio(self, url, title):
        url = 'https:' + url
        response = requests.get(url, headers=self.headers)
        with open('../datas/videos/' + title + '.mp4', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':

    url = 'https://ibaotu.com/shipin/7-0-0-0-0-1.html'
    spider = Ibaotu_Spider()
    spider.get_spider(url)