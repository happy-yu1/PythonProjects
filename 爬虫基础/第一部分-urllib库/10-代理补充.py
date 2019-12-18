#有些网页需要登录后才可以用，爬虫时需要高级验证
from urllib import request,parse,error

from urllib.request import build_opener,ProxyHandler

#不使用代理
url='http://www.httpbin.org/ip'
resp=request.urlopen(url)
# print(resp.read())   #此时显示电脑自带的对应外网的ip


#使用代理后
handler=ProxyHandler({'http':'183.164.238.56:21927'})
opener=build_opener(handler)
try:
    resp1=opener.open(url,timeout=3)
    print(resp1.read())
except error.URLError as e:
    print('timeout')