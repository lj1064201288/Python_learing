'''
爬取爱包图视频
url:https://ibaotu.com/shipin/7-0-0-0-0-1.html
'''

import requests
from lxml import etree

# 构建一个spider类
class Ibaotu_Spider(object):
    # 初始化headers
    def __init__(self):
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_spider(self, url):
        '''
        对接收到的网址进行访问,返回源码
        :param url: 网址
        :return: 源码
        '''
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                self.parse_spider(res.text)
        except Exception as e:
            print(e.args)

    def parse_spider(self, html):
        '''
        对接收到的源码进行处理
        :param html: 源码
        :return: 需要的数据
        '''
        html = etree.HTML(html)
        # 获取视频的链接
        src = html.xpath('//div[@class="video-play"]/video/@src')
        # 获取标题
        title = html.xpath('//a[@class="shade-box"]/span/text()')
        for src, title in zip(src, title):
            self.write_vedio(src, title)

        # 获取下一页的节点
        next_page = html.xpath('//a[@class="next"]/@href')
        # 如果有下一页就继续爬取下一页
        if next_page:
            next_url = 'https:' + next_page[0]
            print(next_url)
            self.get_spider(next_url)
        else:
            print('已经爬取完毕,谢谢使用!')

    def write_vedio(self, url, title):
        '''
        获取到视频链接,以及标题进行保存
        :param url: 视频链接
        :param title: 标题
        :return: None
        '''
        url = 'https:' + url
        response = requests.get(url, headers=self.headers)
        with open('../datas/videos/' + title + '.mp4', 'wb') as file:
            file.write(response.content)

if __name__ == '__main__':
    '''
    主函数,执行函数
    '''
    url = 'https://ibaotu.com/shipin/7-0-0-0-0-1.html'
    spider = Ibaotu_Spider()
    spider.get_spider(url)