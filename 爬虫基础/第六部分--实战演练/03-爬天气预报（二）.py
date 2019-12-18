#之前的操作，运行港澳台地区会发生报错,因为在查看源代码时，港澳台的<table>标签源代码书写不规范，对比如文件 1.txt，此时使用lxml无法进行解析（因lxml的容错能力不是很强），审查时完整的是因为浏览器对源代码进行完善和补充，所以需要用html5lib解析器进行解析，功能类似于浏览器，容错能力最强，需要安装 pip  install html5lib
from lxml import etree
import requests
from bs4 import BeautifulSoup as bs
import re

def parse_detail_page(url):
    Header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    res=requests.get(url,headers=Header)
    html=res.content.decode('utf-8')
    # print(html)
    soup=bs(html,'html5lib')

#（1）————筛选出所class="conMidtab"的div标签，并保留第一个，因为后几个div不是今天的信息
    div=soup.find('div',class_="conMidtab")
    # print(type(div),div)

#（2），找到该div下面的所有table标签
    tables=div.find_all('table')
    # print(tables[0])

#（3）
    results=[]
    for table in tables:
        trs = table.find_all('tr')[2:]  # 法二
        for tr in trs:

            city = tr.find('td', width="83").a.text

            low_temp=tr.find('td',width="86").text

            result={'city':city,'low_temp':low_temp}
            results.append(result)
    print(results)
    print('----'*30)

def spider():
    # url='http://www.weather.com.cn/textFC/gat.shtml'
    urls=['http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml']
    for i in urls:
        parse_detail_page(i)

    # parse_detail_page(url)

if __name__ == '__main__':
    spider()