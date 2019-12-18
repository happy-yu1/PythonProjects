import requests

#一、创建session对象
session=requests.session()

'''
#案例：访问智联招聘某个具体招聘信息为例，也是先登录才能访问(成功）

#二、登录
url='https://passport.zhaopin.com/login'  #登录界面的网址
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
date = {'uer_name': '17320063569', 'pw': 'zz01101128.'}
session.post(url,data=date,headers=header)
#三、访问职位信息
position_url = 'https://jobs.zhaopin.com/CC885512760J00225302911.htm'

resp=session.get(position_url)
#
# print(resp.text)
with open('hh.html','w',encoding='utf-8') as f:
    f.write(resp.text)
'''
#案例：访问163邮箱为例，也是先登录才能访问(失败，与人人网一样）
url='https://mail.163.com/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
date = {'uer_name': 'hai5555ping@163.com', 'pw': 'zz01101128.'}
session.post(url,data=date,headers=header)
user_url='https://mail.163.com/js6/main.jsp?sid=IBDepEJAUXCRzOccIuAAHRMyoSjwonKM&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'
resp=session.get(user_url)
# print(resp.content.decode('utf-8'))
with open('hh.html','w',encoding='utf-8') as f:
    f.write(resp.text)