#对结果进行可视化分析，用到pyecharts包，需要下载并导入pyecharts
from typing import Iterable

from lxml import etree
import requests
from bs4 import BeautifulSoup as bs
import re
# from pyecharts.charts import Bar    # Bar为柱状图
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType #导入主题
results=[]
def parse_detail_page(url):
    Header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    res=requests.get(url,headers=Header)
    html=res.content.decode('utf-8')
    soup=bs(html,'html5lib')
    div=soup.find('div',class_="conMidtab")
    tables=div.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for tr in trs:
            city = tr.find('td', width="83").a.text
            # low_temp=tr.find('td',width="86").text

            low_temp = int(tr.find('td', width="86").text)
            result={'city':city,'low_temp':low_temp}
            results.append(result)
    # print(results)
    # print('----'*30)

def spider():

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
    results.sort(key=lambda date:date['low_temp'])
    # print(results)
    ten_city=results[0:10]
    # print(ten_city)
#数据可视化

#（2）将十个城市的名字放在一个列表中
    cities=[]
#法一：
    # for i in ten_city:
    #     city=i['city']
    #     cities.append(city)
#法二：使用map(func,ten_city)函数,其中func为一个函数，ten_city是等待遍历的变量，每一个元素i要传入func（)函数进行处理
    cities=list(map(lambda i:i['city'],ten_city))  #返回的是一个map，可进行迭代，通过list方式转换成列表
    # print(cities)
    city_temp=list(map(lambda i:i['low_temp'],ten_city))
# （1）创建一个柱状图
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 设置表格名字
    bar.add_xaxis(cities)   #添加x坐标
    bar.add_yaxis('气温',city_temp)   #添加y坐标
    # bar.set_global_opts(title_opts=opts.TitleOpts(title="城市最低气温排行榜")) #创建主标题
    bar.set_series_opts( visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="城市最低气温排行榜"))
    bar.render('temper.html')  #将结果放在一个网页中


if __name__ == '__main__':
    spider()