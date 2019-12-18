#安装 pip install bs4（或beautifulsoup4）
from bs4 import BeautifulSoup
import requests

hh="""
<p>我是小狗</p>
<tr>大坏蛋<a href='hello' mb='maya'></a></tr>
<b><hhh></b>
<a href='我的'></a>
"""
# soup=BeautifulSoup(hh,'lxml')    #使用css选择器
# # print(soup.b.string)  #获取不到内容，因为包含了<hhh>
# print(soup.a.attrs)  #获取第一个a标签的所有属性，以字典形式——href='hello' mb='maya'
# print(soup.a.attrs['href'])  #不一定从第一个a标签开始匹配
# print(soup.a['href'])  #获取a标签href属性对应的值

# url='https://zhidao.baidu.com/question/246019942011070764.html'
# res=requests.get(url)
# html=res.text
# soup=BeautifulSoup(html,'lxml')
# print(soup.div.attrs['id'])
tex=''' <p><h>我的<h1>我们的</h1></h></p><p><h2>你的</h2></p>'''
soup=BeautifulSoup(tex,'lxml')
# print(soup.p.h2)   #结果为None
print(soup.p.h1)