from urllib import request, parse

from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor
import http.cookiejar,urllib.error

# 一、登录人人主页
renren_url = 'http://www.renren.com/'
cookie = http.cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = build_opener(handler)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

date = {'uer_name': '17320063569', 'pw': '01101128'}
req = request.Request(url=renren_url, data=parse.urlencode(date).encode('utf-8'), headers=header)
# try:
#     opener.open(req)   #这一步就出问题了，要访问网站人人网登录网站，拒绝访问
# except urllib.error.HTTPError as e:
#     print(e.code)

# 访问大鹏主页
dapeng_url = 'http://www.renren.com/880151247/profile'

try:
    req = request.Request(dapeng_url, data=parse.urlencode(date).encode('utf-8'), headers=header)
    print('oo')
    resp = opener.open(req)   #禁止打开，反爬虫
    print('pp')
    with open('dapeng_renren.html', 'w') as f:
        f.write(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.reason)
