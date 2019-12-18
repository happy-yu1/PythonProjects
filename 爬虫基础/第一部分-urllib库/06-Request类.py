from urllib import request
from urllib import parse

#一、若采用之前的urlopen（）函数获取拉勾网上的代码，会出现不完整现象，因为存在反爬虫
url='https://www.lagou.com/zhaopin/Java/?labelWords=label'
# req1=request.urlopen(url)
# print(req1.read())

# print('------'*5)
#二、采用Request类进行读取：比如添加User-Agent请求头
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

re=request.Request(url,headers=header)  #添加请求头
req2=request.urlopen(re)
print(req2.read())    #此时捕捉到的代码要更加的完全

