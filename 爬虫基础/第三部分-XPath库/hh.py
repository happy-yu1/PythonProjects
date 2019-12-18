from lxml import etree
import requests
from bs4 import BeautifulSoup

# a='12中国'
# b=a.encode('utf-8')
# b2=a.encode('gbk')
# print(b)
# print(b2)
url='https://zhidao.baidu.com/question/246019942011070764.html'
res=requests.get(url)
html=res.text
soup=BeautifulSoup(html,'lxml')
print(soup.div.attrs)