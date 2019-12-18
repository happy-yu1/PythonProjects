#有些网页需要登录后才可以用，爬虫时需要高级验证
from urllib import request
import urllib.parse

from urllib.request import build_opener,ProxyHandler
from urllib.error import URLError

#ProxyHandler是创建代理服务器的；；；

# url='https://www.baidu.com/'
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
proxy_handler=ProxyHandler({'http':'http://182.35.86.118:9999'})

#使用Request类进行请求，降低反爬虫
opener=build_opener(proxy_handler)
header={'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
date1 = {'first': 'true', 'pn': '1', 'kd': 'python'}
date2=urllib.parse.urlencode(date1).encode('utf-8')
req=request.Request(url=url,headers=header,method='GET')

# resp=opener.open(req)
# print(resp.status)
try:
    resp=opener.open(req)
    print(resp.read().decode('utf-8'))
    # print(resp.statue)
except URLError as e:
    print(e.reason)

