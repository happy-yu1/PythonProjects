#以中国天气网为例，爬取某天  每个城市的最低温度，并进行对比
from lxml import etree
import requests
from bs4 import BeautifulSoup as bs
import re

def parse_detail_page(url):
    Header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    res=requests.get(url,headers=Header)
    html=res.content.decode('utf-8')   #用.text时中文不显示，所以换成context
    # print(html)
    soup=bs(html,'lxml')

#（1）————筛选出所class="conMidtab"的div标签，并保留第一个，因为后几个div不是今天的信息
#法一：使用select方法进行筛选
    # div=soup.select('div .conMidtab')[0]
#法二：使用find方法，find方法只找第一个
    div=soup.find('div',class_="conMidtab")
    # print(type(div),div)

#（2），找到该div下面的所有table标签
 #法一：
#   tables=div.selcet('table')
 #法二：
    tables=div.find_all('table')
    # print(tables[0])  #第一个table显示的是北京的信息
#（3）找到table标签下的tr标签，前两个是无用信息，从第三个开始
    results=[]
    for table in tables:
        # trs = table.select('tr')[2:]   # 法一
        trs = table.find_all('tr')[2:]  # 法二
        # print(trs)
        # break
#（4）分析tr标签，找到下面包含城市名字和最低气温的td标签，城市名字位于第一个td的文本中，最低气温位于第8个td标签的文本中，根据下标进行内容提取
        for tr in trs:

# 4.1获取城市名

#法一：用select方法获取到的所有a标签信息，以列表的形式保存下来，若想获得a标签中的文本，需要进行遍历然后再提取，比较麻烦
            # A=tr.select('td[width="83"] > a')
            # for a in A:
            #     city=a.text
            #     print(city)
# 法二：不可以用find_all()方法，以上操作带来的结果携带\n，如：'city': '\n北京',通过sub方法将其替换掉。
            # city=tr.find('td',width="83").text
            # city=re.sub('\n','',city)
#法三：
# 3.1 以下标的方式在爬取其他页面时容易出现问题
            # city_td=tr.find_all('td')[0]   #提取第一个td标签
    #获取该td标签下所有的文本信息，且不包含空格，但返回的是一个生成器，转换成list格式——['北京']，每个结果只包含一个文本，即城市名，所以用下标的方式提取出来
            # city = list(city_td.stripped_strings)[0]
            # print(city)    # 北京
#换成东北地区的网页时，输出结果为{'city': '黑龙江', 'low_temp': '-15'}, {'city': '齐齐哈尔', 'low_temp': '-18'}, 而正确的应该是{'city': '哈尔滨', 'low_temp': '-15'}, {'city': '齐齐哈尔', 'low_temp': '-18'}，

# 3.2解决办法：思路：黑龙江省里面城市排序为：哈尔滨、齐齐哈尔…… ，一个tr信息代表一个城市，每个tr下面有多个td标签。第一个tr标签下的第一个td里存放的是“黑龙江省”，第二个td里存放的是“哈尔滨”。第二个开始往后的每个tr标签下的第一个td里存放的是“城市名”。所以
#         for index,tr in enumerate(trs):
#             tds=tr.find_all('td')
#             if index==0:  #如果是第一个tr
#                 city_td=tds[1]   #取第二个td标签
#             else:
#                 city_td = tds[0]  #其它的tr标签，取第一个td标签
#             city=list(city_td.stripped_strings)[0]
            # print(city)
#结果为：{'city': '哈尔滨', 'low_temp': '-15'}, {'city': '齐齐哈尔', 'low_temp': '-18'}

#法四（最好）：因为a标签正好属于目标tr标签的直接子标签，可通过目标tr.a.text的方式将a中的文本提取出来
            city=tr.find('td',width="83").a.text

# 4.2获取最低气温
            low_temp=tr.find('td',width="86").text

# 4.3将城市和对应的温度汇总在一个字典内，并添加到总的结果中去
            result={'city':city,'low_temp':low_temp}
            results.append(result)
    print(results)

def spider():
    url='http://www.weather.com.cn/textFC/xn.shtml'
    # urls={'hb_url':'http://www.weather.com.cn/textFC/hb.shtml',
    #     # 'db_url':'http://www.weather.com.cn/textFC/db.shtml',
    #     # 'hd_url':'http://www.weather.com.cn/textFC/hd.shtml',
    #     # 'hz_url':'http://www.weather.com.cn/textFC/hz.shtml',
    #     # 'hn_url':'http://www.weather.com.cn/textFC/hn.shtml',
    #     # 'xb_url':'http://www.weather.com.cn/textFC/xb.shtml',
    #     # 'xn_url':'http://www.weather.com.cn/textFC/xn.shtml',
    #     # 'gat_url':'http://www.weather.com.cn/textFC/gat.shtml'}
    #     # for i in urls:
    #     #     parse_detail_page(urls[i])

    parse_detail_page(url)


if __name__ == '__main__':
    spider()