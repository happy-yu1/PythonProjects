from lxml import etree
import re
#douban.html 里面存放的是电影列表的信息，并非网页全部信息
#一、将信息解码,获得规范的html信息
parse=etree.HTMLParser(encoding='utf-8')
html=etree.parse('douban.html',parser=parse)
#可以将html信息输出看看
# print(html)，此时为一个element对象，若要查看具体详情，需要进行解码print（etree.tostring(htmlE,encoding='utf-8').decode('utf-8')）

#二、提取所有class属性=item的div标签
a=html.xpath('//a[@class="item"]')
# print(a)  #  输出为一个列表，每个元素是一个element对象
'''
for i in a :
    print(i)
    print(etree.tostring(i, encoding='utf-8').decode('utf-8'))
# 通过遍历的方法可得到a中的每个对象，通过print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
'''
movies=[]
for i in a:
    movie_href1=i.xpath('@href')[0]#获得a标签中的href属性，即电影链接
    movie_href=re.sub('热门&from=gaia.*','',movie_href1)
#因为movie_href1得到的答案：'https://movie.douban.com/subject/26709258/?tag=热门&from=gaia_video。其中‘热门&from=gaia_video’并非想要的内容，需要用sub方法替换掉。
    photo=i.xpath('.//img/@src')[0] #获得改i标签下的image标签的src属性内容，即海报缩略图
    name=i.xpath('.//img/@alt')[0]  #获得该i标签下的image标签的alt属性内容，即电影名
    score = i.xpath('.//strong/text()')[0] #获得strong标签下的文本，即评分
#[0]的作用是因为，i.xpath得到的是一个列表，而这个列表只包含了一个元素，通过下标的方式将结果提取出来
    movie={'movie_url':movie_href,'picture':photo,'movie_name':name,'score':score}
    movies.append(movie)
print(movies)