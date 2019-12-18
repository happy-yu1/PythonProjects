from urllib import request
from urllib import parse
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# 二、采用Request类进行读取：比如添加User-Agent请求头
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36','Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}

date1 = {'first': 'true', 'pn': '1', 'kd': 'python'}
date2=parse.urlencode(date1) #利用urlencode方法发送请求数据编码
date3=date2.encode('utf-8') #将发送的请求数据编码成字节数组，
#或方法：date3=bytes(date2,encoding='utf-8')

re = request.Request(url,data=date3, headers=header,method='POST')  # 添加多个参数,尽可能降低被识别出爬虫程序
req2 = request.urlopen(re)
print(req2.read().decode('utf-8'))  # 查看返回数据
# print(req2.status)