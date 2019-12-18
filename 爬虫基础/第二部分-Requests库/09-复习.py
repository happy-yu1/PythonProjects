import requests,re
from urllib import parse,request
url='https://www.douban.com/photos/album/1647622767'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

'''
#requests库中响应对象获取状态码的方法
resp=requests.get(url,headers=header)
print(resp.status_code)
'''
#urllib库中，request模块中响应对象获取状态码的方法：

rep=request.Request(url,headers=header)
resp=request.urlopen(rep)
print(resp.getcode())
print(requests.codes.ok)