from urllib import parse, request
from http.cookiejar import CookieJar

# 生成一个cookie对象
cookie = CookieJar()
# 生成一个cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 绑定cookie管理器
opener = request.build_opener(cookie_handler, http_handler, https_handler)


def login_huawei(user, password):

    base_url = "https://www.huawei.com/en/accounts/LoginPost"

    data = {
        'userName': user,
        'pwd': password,
        'fromsite': 'www.huawei.com',
        'authMethod':'password'
    }

    data = parse.urlencode(data)
    response = request.Request(base_url, data=bytes(data, 'utf-8'))
    content = opener.open(response)
    print(content.read().decode())

if __name__ == '__main__':
    user = input('请输入账号:')
    password = input('请输入密码:')

    login_huawei(user, password)