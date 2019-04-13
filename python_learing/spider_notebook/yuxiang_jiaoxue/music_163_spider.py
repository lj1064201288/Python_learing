'''
网易云音乐图形界面下载歌曲
音乐下载地址
url: https://music.163.com/song/media/outer/url?id=
获取页面源码:
https://music.163.com/playlist?id=2742358993
'''

import requests, random
from tkinter import *
from urllib import request
from bs4 import BeautifulSoup



headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Host': 'music.163.com',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': '1'
}

def music_spider():
    # 获取用户输入的地址
    # url = entry.get()
    url = "https://music.163.com/playlist?id=2742358993"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    # print(soup.prettify())
    items = soup.find_all('a')
    print(items)
    # for item in items:
    #     print(item.find_all('span'))


def music_quit():
    pass

# 创建窗口
root = Tk()
# 设置标题
root.title('网易云音乐下载')
# 设置窗口大小
root.geometry('800x450')
# 设置界面位置
root.geometry('+550+240')
# 设置下载标签:请输入你的下载地址
lable = Label(root, text='请输入你的网址:', font=('仿宋', '15'))
# 定位 pack, grid, palce
lable.grid()

# 设置第一个输入鲁昂
entry = Entry(root, font=('微软雅黑', '15'), width=60)
# 定位
entry.grid(row=0, column=1)

# 设置列表框
text = Listbox(root, font=('微软雅黑', '15'), width=76, height=15)
text.grid(row=1, columnspan=2)

# 设置按钮
button1 = Button(root, text='Start', font=('微软雅黑', 20), command=music_spider)
button1.grid(row=2, column=0, sticky='s')
# 退出按钮
button2 = Button(root, text='Quit', font=('微软雅黑', 20), command=music_quit)
button2.grid(row=2, column=1)

root.mainloop()
