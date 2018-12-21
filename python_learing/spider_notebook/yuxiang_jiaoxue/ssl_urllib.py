import ssl
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://inv-veri.chinatax.gov.cn/'

#url = "https://www.csls.cdb.com.cn/"
print(url)
response = request.urlopen(url)
print(response.status)
html = response.read().decode('GBK')
print(html)