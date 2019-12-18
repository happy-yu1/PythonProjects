#提取出前10个气温最低的城市
#思路：先将获得的最低气温进行排序————从结果中获取前10个城市
from lxml import etree
import requests
from bs4 import BeautifulSoup as bs
import re,csv
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
    #因为排序时需要数值型的，所以讲字符串格式的最低气温转换成数值型的
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
    results.sort(key=lambda date:date['low_temp'])  #将所有城市的气温进行排序
    # print(results)
    ten_city=results[0:10]   #提取前10个城市
    # print(ten_city)
#可将结果储存在CSV文件
    header=['city','low_temp']
    with open('city.csv','w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,header)
        writer.writeheader()
        writer.writerows(ten_city)


if __name__ == '__main__':
    spider()