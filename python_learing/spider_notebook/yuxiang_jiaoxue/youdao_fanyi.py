import json,random, time, math
from hashlib import md5
from urllib import request, parse


# var r = function(e) {
#         var t = n.md5(navigator.appVersion)
#           , r = "" + (new Date).getTime()
#           , i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
#         }
#     };

agents = [
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
]

def fanyi_youdao(key):

    '''
    r = "" + (new Date).getTime()
    t = n.md5(navigator.appVersion)
    i = r(t)
    :param key:
    :return:
    '''

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        'i': key,
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'smartresult': 'dict'
    }

    data = parse.urlencode(data)

    headers = {
        'Accept':'application/json,text/javascript,*/*;q=0.01',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':len(data),
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':agent
    }

    req = request.Request(url,headers=headers, data=bytes(data,encoding='utf-8'))
    print(req)
    try:
        response = request.urlopen(req)
        if response.status == 200:
            print('111')
            html = response.read().decode('utf-8')
            print(html)
    except Exception as e:
        print(e)


def salt():
    date = time.time()
    salt = int(date*1000) + random.randint(0,10)
    print(salt)
    return math.ceil(salt)

def sign(key):
    a = 'fanyideskweb'
    b = 'p09@Bn{h02_BIEe]$P^nG'
    md = md5()
    md.update(bytes(key, encoding='utf-8'))
    s = ''

    sign = md5((a + key + str(salt) + b).encode('utf-8')).hexdigest()
    return sign




if __name__ == '__main__':

    i = input('请输入你要翻译的内容:')
    agent = random.choice(agents)
    salt = salt()
    sign = sign(i)
    ts = time.time() * 10000
    bv = md5(agent.encode('utf-8')).hexdigest()
    fanyi_youdao(i)
