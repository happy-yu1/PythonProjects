#以凤凰网上的军事新闻为例，爬取每条新闻的详细信息：题目和详情介绍
import json,csv
import re
import requests
from bs4 import BeautifulSoup as bs
'''
<div class="news-stream-newsStream-news-item-infor"><h2 class="news-stream-newsStream-mr13 news-stream-newsStream-news-item-title news-stream-newsStream-news-item-title-height"><a href="//mil.ifeng.com/c/7rrJVGaafWy" title="都说秦军无胄，为何连汉军重骑兵都没头盔？从复原画解析秦汉武备" target="_blank">都说秦军无胄，为何连汉军重骑兵都没头盔？从复原画解析秦汉武备</a></h2><div class="clearfix"><span class="news-stream-newsStream-mr10 news-stream-newsStream-text">冷兵器研究所</span><time class="news-stream-newsStream-text">今天 11:12</time><a class="news-stream-newsStream-ly ly" id="count6604201860309983232" href="https://gentie.ifeng.com/view.html?docUrl=ucms_7rrJVGaafWy&amp;docName=都说秦军无胄，为何连汉军重骑兵都没头盔？从复原画解析秦汉武备&amp;skey=865042&amp;pcUrl=https://mil.ifeng.com/c/7rrJVGaafWy" target="_blank">0</a></div></div>
'''

#用最原始的样式匹配的方法进行解析。
# 如果某些需要的详情信息存放在Java脚本中，通过对该脚本中的内容进行解析获得相关详情，仍需要用到re库中的相关内容进行内容匹配。
def get_pagedate(url):

    head={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res=requests.get(url,headers=head)
    html=res.text
    # print(html)


    """

    # 法一：用BeautifulSoup方法进行解析——————————不适用
    # soup=bs(html,'lxml')
    # print(soup)
    # detail = soup.select('div h2 a') #筛选不出上面的a标签——不可行
    # detail=soup.select("script") #有内容
    # print(detail)

# 通过这种方法，筛选不出任何信息，因为审查元素时，相关信息显示存在div下的h2中的a标签里面，但是查看源代码时，相关信息统统放在放在Java脚本 <script>中的 var allData = 中，这是真实信息存放的地方即：
# <script>
#         var allData = {"channel":[{"logo":"https://p3.ifengimg.com/37780e23b9ea2d8b/2017/38/logoMil.png","title":"军事","domain":"mil.ifeng.com"},{"title":"军情热点"}],"nav":………………

#法二、使用re方法进行匹配，匹配var allData =后的所有内容，以便进一步解析
    # 这种方法只匹配打这几个代码，后续代码匹配不到————————放弃
    r = re.search('var allData =', html)  
    print(r)
"""
#法三、因为存放目标元素的var allData =…………一串代码在一行上，所以通过对源代码进行按行拆分
    lines=html.split('\n')
    for line in lines:
        if re.search('var allData =',line) !=None:
            print(type(line),line)
#于是将包含目标代码的那一串信息提取出来了：var allData ={………} ,变量var allData是一个str

#后续操作则为   06-spidernews练习.py 中的内容：将json对象{……}转换成pyhton中的dict对象

if __name__ == '__main__':
    url = "https://mil.ifeng.com/shanklist/14-35083-"
    get_pagedate(url)