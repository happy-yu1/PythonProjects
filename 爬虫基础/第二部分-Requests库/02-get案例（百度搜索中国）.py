import requests
from urllib import parse

url='https://www.baidu.com/s'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
params={'wd':'中国'}
resp=requests.get(url,params=params,headers=header)
with open ('baidu.html','w',encoding='utf-8') as f:
    f.write(resp.content.decode('utf-8'))
print(resp.url)

