import json, random, tkinter
from urllib import request, parse

def fanyi():
    base_url = "https://fanyi.baidu.com/sug"
    agent = random.choice(agents)
    kw = searchEntry.get()
    data = {
        'kw': kw
    }
    data = parse.urlencode(data)

    headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept-Language': 'zh - CN, zh;q = 0.9 Connection: keep - alive',
        'User-Agent':agent,
        'Host':'fanyi.baidu.com',
        'Origin':'https://fanyi.baidu.com',
        'Referer':'https://fanyi.baidu.com/',
        'Content-Length': len(data)
    }
    try:
        req = request.Request(base_url, headers=headers, data=bytes(data, encoding='utf-8'))
        response = request.urlopen(req)
        html = response.read().decode()
        json_datas = json.loads(html)
        items = json_datas.get('data')
        for item in items:
            showLabel = tkinter.Label(base, text=item['k'] + '----' + item['v'])
            showLabel.pack()
            searchEntry.delete(0, tkinter.END)

            #print(item['k'] + '----' + item['v'])
    except Exception as e:
        searcherror = tkinter.Label(base, text=e.args)
        searcherror.pack()
        #print(e.args)


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




    base = tkinter.Tk()
    base.wm_title('百度翻译')
    searchLabel = tkinter.Label(base, text='请输入要翻译的内容:', background='red', fg='white')
    searchEntry = tkinter.Entry(base)
    searchEntry.pack()
    searchLabel.pack()
    btn = tkinter.Button(base, text='搜索', command=fanyi, background='red', foreground='white')
    btn.pack()

    base.mainloop()