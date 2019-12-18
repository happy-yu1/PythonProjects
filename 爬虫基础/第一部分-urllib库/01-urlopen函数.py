'''
# encoding:utf-8
from urllib import request,parse
resp=request.urlopen('https://mail.163.com/')
# print(resp.getcode())
# print(type(resp))
txt=resp.read()
# print(type(txt))
# print(txt.decode('utf-8'))
print(resp.status)  #status属性，获取当前状态码
# print(resp.msg)
print(resp.reason)
print(resp.getheaders())
print(resp.getheader('Content-Type'))  #获取‘Content-Type’所对应的内容
'''


#一、date属性
'''url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
date1 = {'first': 'true', 'pn': '1', 'kd': 'python'}
date2=parse.urlencode(date1) #利用urlencode方法发送请求数据编码
date3=date2.encode('utf-8') #将发送的请求数据编码成字节数组，
#或方法：date3=bytes(date2,encoding='utf-8')
req2 = request.urlopen(url,data=date3)
print(req2.read().decode('utf-8')) 
'''

#二、timeout属性
from urllib import request,parse,error
import socket

try:
    resp = request.urlopen('https://mail.163.com/',timeout=0.01)
    print('连接成功')
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('连接超时')