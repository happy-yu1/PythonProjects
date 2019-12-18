#安装 pip install bs4（或beautifulsoup4）
from typing import Iterable


from bs4 import BeautifulSoup
import requests


url='https://zhidao.baidu.com/question/246019942011070764.html'
res=requests.get(url)
html=res.content.decode('gbk')
soup=BeautifulSoup(html,'lxml')

'''
print(soup.div.a)  
#1、此种方法只能找到满足条件的第一个元素，只能查找一个，获取多个则需要用BS传统方法层层筛选，较麻烦

#2、获取多个目标标签时
# t=soup.find_all('div',attrs={'class':"head-wrap"})
t=soup.find_all('header',attrs={'class':"container"})
# print(t)

print(type(t),len(t),t,sep='\n')  #此时t的类型是bs4.element.ResultSet'

# print(isinstance(t,Iterable))  #返回True，是可遍历的对象
#按住alt和enter可以导入Iterable（可遍历类型）。isinstance函数可以判断t是否属于可遍历对象。
for i in t:
    print(i)

#因为t并不是tag类型的，无法在这种类型基础上再使用find_all、find等方法进一步的查找下去
# a=t.find_all('a')    #会报错
# print(len(a))

'''
#3、正确做法如下：
#一、将获得的div标签即t变量转变成str形式
t=soup.find_all('header',attrs={'class':"container"})
div=str(t)

#二、利用div字符串实例化成一个BeautifulSoup对象
soup2=BeautifulSoup(div,'lxml')
#三、对上面的结果再进行查询，获得div标签下的a标签
a=soup2.find_all('a')
# print(type(a),a,sep='\n')
print(a)

#因为BS自带的方法查询比较麻烦，一般需要搭配新增的select方法进行解析

