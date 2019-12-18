import requests

'''
#拉勾网请求
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36','Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='}
date = {'first': 'true', 'pn': '1', 'kd': 'python'}

resp=requests.post(url,data=date,headers=header)
# with open ('baidu.html','w',encoding='utf-8') as f:
#     f.write(resp.content.decode('utf-8'))
print(resp.content.decode('utf-8'))
'''
#智联招聘
url = 'https://sou.zhaopin.com/?jl=%E5%8C%97%E4%BA%AC&sf=0&st=0&kw=Java%E5%BC%80%E5%8F%91&kt=3'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
date = {'first': 'true', 'pn': '1', 'kd': 'python'}

resp=requests.get(url,headers=header)
# with open ('baidu.html','w',encoding='utf-8') as f:
#     f.write(resp.content.decode('utf-8'))
print(resp.content.decode('utf-8'))