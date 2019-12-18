#有些网页需要登录后才可以用，爬虫时需要高级验证
from urllib import request,parse
from urllib.request import build_opener
import http.cookiejar

'''
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
cookie=http.cookiejar.CookieJar()  #创建一个空的cookie对象，用于存放爬到的cookie数据

handler=request.HTTPCookieProcessor(cookie)
opener=build_opener(handler)  #创建一个opener
resp=opener.open(url)
# print(resp.read().decode('utf-8'))
for item in cookie:
    print(item.name+'='+item.value)

#将cookie文件保存在本地，以txt文件的形式，以百度网页为例，此法仅适用简单的网页，反爬虫比较厉害的网页，如需要登录的网页需要添加相应的请求头之类的信息伪装一下

url='https://www.baidu.com/'
filename='cookies.txt'  #会在本地创建一个txt文件保存爬到的cookie数据
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=request.HTTPCookieProcessor(cookie)
opener=build_opener(handler)  #创建一个opener
resp=opener.open(url)
cookie.save(ignore_discard=True,ignore_expires=True)


#采用LWPCookiejar方法进行cookies文件的读取和保存
url='https://www.baidu.com/'
filename='cookies.txt'  #定义时为txt文件
cookie=http.cookiejar.LWPCookieJar(filename) #将txt文件的cookie转化为LWP格式
handler=request.HTTPCookieProcessor(cookie)
opener=build_opener(handler)  #创建一个opener
resp=opener.open(url)
print(resp.read().decode('utf-8'))
'''

# 采用load方法获取本地cookie文件的内容
url='https://www.baidu.com/'
cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
#此时获取本地的cookies.txt文件
handler=request.HTTPCookieProcessor(cookie)
opener=build_opener(handler)  #创建一个opener
resp=opener.open(url)
print(resp.read().decode('utf-8'))