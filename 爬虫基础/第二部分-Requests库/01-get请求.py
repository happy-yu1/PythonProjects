import requests
from urllib import parse
#一、了解get请求的属性
'''url='https://www.baidu.com/'
url1='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
resp=requests.get(url)
# print(resp.content.decode('utf-8'))

print(resp.status_code)  #获取状态码
print(resp.text)  #服务器返回的响应文本——里面会有乱码
print(type(resp.text))   #服务器返回的响应文本类型——————str


#用get传递参数
url='http://www.httpbin.org/get'
date={'name':'哈哈','age':12}
resp=requests.get(url,params=date)
resp=requests.post(url,data=date)
print(resp.text)
'''

#返回json格式
url='http://www.httpbin.org/get'
date={'name':'哈哈','age':12}
resp=requests.get(url,params=date)

print(resp.json())   #直接将“哈哈”输出
print(type(resp.json()))

# print(resp.text)   #将“哈哈”进行编码后输出
# print(parse.parse_qs(resp.text))
# print(type(resp.text))
# print(resp.content.decode('utf-8'))
print(resp.url)  #查看url的地址
print(resp.encoding)