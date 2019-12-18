import requests


url = 'http://www.httpbin.org/ip'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36','Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
proxy={'http':'121.232.148.195:9000'}
resp=requests.get(url,headers=header,proxies=proxy)
# with open ('baidu.html','w',encoding='utf-8') as f:
#     f.write(resp.text)
print(resp.text)


