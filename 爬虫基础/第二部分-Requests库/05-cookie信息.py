import requests


url = 'http://www.baidu.com'


resp=requests.get(url)

print(resp.cookies)
print(resp.cookies.get_dict())  #以字典的形式展现出cookie信息

