#有些网页需要登录后才可以用，爬虫时需要高级验证
from urllib import request,parse
from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener
from urllib.error import URLError

#HTTPPasswordMgrWithDefaultRealm是用来装验证信息的；；；
# HTTPBasicAuthHandler用来解决认证问题的

url='https://mail.163.com/js6/main.jsp?sid=IASRccXpvolYlBxitGpphXbpnTZzcbHB&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'

user_name='hai5555ping@163.com'
pswd='zz01101128.'
p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,user_name,pswd)  #添加用户信息
auth_handler=HTTPBasicAuthHandler(p)  #验证
opener=build_opener(auth_handler)

try:
    re=opener.open(url)
    result=re.read().decode('utf-8')
    print(result)
except URLError as e:
    print(e.reason)
