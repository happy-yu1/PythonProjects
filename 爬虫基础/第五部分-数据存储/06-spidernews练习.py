#以凤凰网上的军事新闻为例，爬取每条新闻的详细信息：题目和详情介绍
import json,csv
import re
import requests
from bs4 import BeautifulSoup as bs

#1、若某些需要的详情信息存放在Java脚本的某个变量中，先提取该变量中的内容再进行解析获得相关详情。如利用凤凰网站提取新闻信息
#2、若查看源代码，所要的详细信息存在于某标签下，则可用之前学的xpath，BeautifulSoup进行解析。如利用网易网站提取相关新闻信息
#3、源代码和审查元素时有时候不会一样，后者可能会进行相关伪装，真实信息存放在源代码中，信息提取时要以源代码为主


def getpagedate(url):
#作用是获取整个页面源代码并返回，其中url是给定的请求url路径，return返回页面源码
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res=requests.get(url,headers=head)
    html=res.text

#因为当前需要解析的所有新闻数据都在JavaScript的 var allData中（审查源代码可以发现，将html按行进行拆分（每行之间使用分隔符\n），而且每条新闻点开后详情信息也都存放在对应的JavaScript的 var allData中
    rows=html.split(sep='\n')
    for row in rows:
        if re.search('var allData',row)!=None:
            # print(row)
            break
#为了方便进一步的解析，将多余的信息包括空格和        var allData = 以及；等不需要的信息替换掉，进而变成json对象{"channel":……，" ",……}   ，json对象可以转换成字典形式的Python对象，进而可以对这个字典对象进行进一步的解析，通过k,v的方式。

    r = re.sub('var allData =|;|/s+', '', row)
    return json.loads(r)

def parse_date(parser):
    """
功能：
    :param parser: 需要解析的字典类型对象
    :return: 获取信息集合,并保存在CSV文件中
    """
    for k in parser:
        if k=='newsstream':

            break
    t=parser[k]  #t是一个列表，包含新闻页面中所有新闻的标题title和详情链接url，日期，
    # print(t)
    # print(len(t)) #共20条新闻
    news=[]
    for i in t: #i事一个字典，每个i为一个新闻
        new={}
        new['title']=i['title']
        new['detali_url']=i['url']
        new['newsTime']=i['newsTime']
        new['source']=i['source']

        # print('-----',i,sep='\n')
        # print(news)
        news.append(new)
    # print(news)
    #提取新闻名和详情链接，存放在news.csv文件中
    header=['title','detali_url','newsTime','source']
    with open('news.csv','w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,header,delimiter=';')

        writer.writeheader()
        writer.writerows(news)



if __name__ == '__main__':
    url="https://mil.ifeng.com/shanklist/14-35083-"
    parser=getpagedate(url)
    # print(type(parser),parser)  #是字典形式的
    parse_date(parser)




