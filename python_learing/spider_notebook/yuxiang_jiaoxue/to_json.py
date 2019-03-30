# import json
#
# str = "[{'username':'daochang', 'age':'18'}]"
#
# json_str = json.dumps(str, ensure_ascii=False)
# print(json_str)
# print(type(json_str))
# new_str = json.loads(json_str)
# print(new_str, type(new_str))

import requests, json
from bs4 import BeautifulSoup

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

r = requests.get('http://seputu.com/', headers=headers)

#print(r.text)

soup = BeautifulSoup(r.text, 'lxml')

content = []
for mulu in soup.find_all(class_="mulu"):
    # 获取标题
    h2 = mulu.find('h2')
    if h2 != None:
        h2_title = h2.string
        # print(h2_title)
        # 获取章节地址与内容
        list = []
        for a in mulu.find(class_="box").find_all('a'):
            href = a.get('href')
            # print(href)
            box_title = a.get('title')
            list.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title, 'content':list})

with open('../datas/tables/gcd.json', 'a', encoding='UTF-8') as f:
    json.dump(content, fp=f, indent=4, ensure_ascii=False)

