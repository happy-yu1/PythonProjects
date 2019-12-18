#安装 pip install bs4（或beautifulsoup4）
from bs4 import BeautifulSoup
hh="""
<dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1277939" title="我和我的祖国" class="image-link" data-act="boarditem-click" data-val="{movieId:1277939}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="我和我的祖国" class="board-img" src="https://p0.meituan.net/moviemachine/b2c5c74d33e45745fd3462e44b3698e18336620.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1277939" title="我和我的祖国" data-act="boarditem-click" data-val="{movieId:1277939}">我和我的祖国</a></p>
        <p class="star">
                主演：黄渤,张译,韩昊霖
        </p>
<p class="releasetime">上映时间：2019-09-30</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">7</i></p>        
    </div>

      </div>
   </div>

                </dd>
"""
soup=BeautifulSoup(hh,'lxml')  #创建一个BeautifulSoup对象，并使用lxml解析器进行解析

# print(soup.prettify())
#使用该方法后，可以观察到新生成的一段代码格式更加规范，多了html标签和body标签，类似于一个dom树

#find_all()方法，获得所有满足条件的内容
# trs=soup.find_all('p')   # 获得所有的img标签
# for i in trs:
#     print(i)
"""
tr=soup.find_all('p')[1]
#返回的是一个生成器，提取当前标签中非标签文本,包括空白，用strip()方法去掉空白
text=tr.string.strip()    
print(text)

"""


tr=soup.find_all('div')[1]
# text=tr.strings  # 返回的是一个生成器，提取所有的子孙标签中非标签文本，包括空白

# text=list(tr.strings) #通过list的方式，将生成器转换成list，存放提取出来的信息
# text=tr.stripped_strings #返回的是生成器，提取所有的子孙标签中非标签文本，不包括空白
# print(list(text))
# for i in text:
#     print(i)
text=tr.get_text()  #get_text()返回的是普通字符串，提取所有的子孙标签中非标签文本
print(text)