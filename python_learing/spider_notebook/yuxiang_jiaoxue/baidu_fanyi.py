import json, random
from urllib import request, parse

def fanyi(kw):
    base_url = "https://fanyi.baidu.com/sug"
    agent = random.choice(agents)

    data = {
        'kw': kw
    }
    data = parse.urlencode(data)

    headers = {
        'User-Agent':agent,
        'Host':'fanyi.baidu.com',
        'Origin':'https://fanyi.baidu.com',
        'Referer':'https://fanyi.baidu.com/',
        'Content-Length': len(data)
    }
    print(len(data))
    try:
        req = request.Request(base_url, headers=headers, data=bytes(data, encoding='utf-8'))
        response = request.urlopen(req)
        html = response.read().decode()
        json_datas = json.loads(html)
        items = json_datas.get('data')
        for item in items:
            print(item['k'] + '----' + item['v'])
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    agents = [
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
    ]


    kw = input('请输入你要翻译的内容:')
    fanyi(kw)