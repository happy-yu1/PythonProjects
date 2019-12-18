from lxml import etree
import requests
#此次实践多页电影信息的提取，结合之前的requets库，html信息通过requests.get()获得
Header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
Base_Domain = 'https://www.ygdy8.net'


#一、获取第一页所有电影对应的详情url
def get_detail_urls(url):
    # url = 'https://www.ygdy8.net/html/gndy/dyzz/index.html'
    resp = requests.get(url, headers=Header)
    text = resp.text  # 用text会出现乱码现象，因为电影天堂的代码不规范，但是不影响提取链接，所以仍用text
    # print(resp.content)
    # print(type(text))
    html=etree.HTML(text)
    detail_urls=html.xpath('//table[@class="tbspan"]//a/@href')
#观察网页的element信息，发现详情url存放在ul的直接子标签table标签下的——子标签a——中的href属性中，所以根据class="tbspan"属性筛选出特性的table标签，再提取table标签下，a标签的href属性，因为第一个a标签的信息并不是我们想要的电影详情url
# print(detail_urls) #此时得到的是str形式的并不是完整的超链接，缺少域名，所以要添加域名
    for detail_url in detail_urls:
        detail_url=Base_Domain+detail_url #得到首页展示电影对应的详情url
        print(detail_url)

#二、根据url详情超链接获取对应的信息：电影名，海报，年份，演员,下载链接等

# def parse_detail_page(url):
#1、该url为上面得到的detail_url,下面对这个链接里面的信息进行提取，以某个具体详情页url，最终代码不需要这个例子，只是为了方便查看相关内容
url = 'https://www.ygdy8.net/html/gndy/dyzz/20191030/59293.html'
movie={}
resp=requests.get(url,headers=Header)
text=resp.content.decode('gbk') # 此处应该用content的方式进行，text的话提取信息会有乱码
# print(text) #通过信息输出，判断用text，还是content哪个更合适
html=etree.HTML(text)

title=html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
# print(title)
movie['title']=title  #提取电影名

#2、观察其他信息，如海报，剧情截图等img链接、演员、简介等内容存放在属性id=“Zoom”的div标签中
zoomE=html.xpath('//div[@id="Zoom"]')[0]   #将信息提取出来，否则是列表形式
imgs=zoomE.xpath('.//img/@src')
#在上面提取的div标签下，再查询img标签，并提取出img标签对应的src属性，此处要用.//的形式，表明是在当前节点再进行xpath，否则默认为在全网页中寻找src属性
# print(imgs)

#会出现两个结果，因为该详情链接中有海报图，还有剧情介绍图。要分别提取出来
cover=imgs[0]
movie['cover']=cover  #提取海报图
screenshot=imgs[1]
movie['screenshot']=screenshot #提取截图

#3、提取年份和演员列表，这些信息均存放于zoomE标签下的文本中，而且前面都有◎标志，如‘◎年　　代’，用text（）的方式提取出来，并根据◎标志进行信息筛选和提取
infos=zoomE.xpath('.//text()')
# print(infos)
def parse_rule(info,rule):
    return info.replace(rule,'').strip()
for index,info in enumerate(infos):  #解释在下面，主演信息那
    if info.startswith('◎年　　代'):
        info=parse_rule(info,'◎年　　代')
        movie['year']=info   #提取年份

    elif info.startswith('◎主　　演'):
        actors=[]
        info=parse_rule(info,'◎主　　演')  #提取 杰森·苏戴奇斯 Jason Sudeikis
        actors=[info]
        # print(actors)
# 因为与◎主　　演同行的只有一个演员：杰森·苏戴奇斯 Jason Sudeikis，其他演员一次往后排，上面方法只能提取出杰森·苏戴奇斯 Jason Sudeikis，其他的提取不出来。观察网页的展示的信息可知，infos中提取的中文信息按行进行排序，每行有自己的index序号，第一行的index=1，第二行的index=2，以此类推，所以需要在之前添加enumerate（）函数，该函数有两个参数：index和info，其中info为存入的信息，index为该信息的序号。
        for x in range(index+1,len(infos)):
            # 因为与◎主　　演同行的演员姓名已经提取出来，需要从下一行接着提取，所以从index+1开始，因为后面有多少行没有数，所以以infos列表的长度为终。
            actor=infos[x].strip()
#此时提取出来的actor信息不仅包含后面的演员名字，还会包含演员信息后的◎标　　签，◎简　　介等其他信息，这是因以infos列表的长度为终导致的。解决办法就是将所有演员姓名提取出来后结束for循环。因此，可以以‘◎’为标志，来设计break，遇到◎，循环就截止。
            if infos[x].startswith('◎'):
                break
            actors.append(actor)   #提取其他演员的姓名
        movie['actors']=actors  #提取所有演员的名字

    elif info.startswith('◎简　　介'):  #原理同上
        details=[]
        for x in range(index+1,len(infos)):
            introduction =infos[x].strip()
            # print(introduction)

            if infos[x].startswith(' '): #因为简介完了之后是是空行，可以设置遇到空行就结束for循环
                break
            details.append(introduction)
        movie['details']=details   #提取电影简介

print(movie)





