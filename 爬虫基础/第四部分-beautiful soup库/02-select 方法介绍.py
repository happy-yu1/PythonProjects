#安装 pip install bs4（或beautifulsoup4）
from bs4 import BeautifulSoup


hh="""
<dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="霸王别姬" class="board-img" src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
           主演：张国荣,张丰毅,巩俐 
          
        </p>
<p class="releasetime">上映时间：1993-07-26</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""
soup=BeautifulSoup(hh,'lxml')    #使用css选择器
print(type(soup))
print(soup.p) #获取一个p标签
print(soup.find('p'))  #获取一个p标签,和soup.p一样
# bs4.BeautifulSoup'类型  是一个DOM树（格式没有优化），在hh的基础上增加了html和body标签
# print(soup)

# print('*'*20)
# t=soup.prettify()
# print(type(t))
#返回的是一个字符串，内容是一个（格式优化）的DOM树，在hh的基础上增加了html和body标签
"""
ps=soup.select('p') #选中所有p标签
print(type(ps))     #list类型
i=ps[1]
print(type(i))  #i为tag类型
print(type(i.string))   # 为NavigableString类型
print(i.string)   #结果为：主演：张国荣,张丰毅,巩俐
# print(i.contents)  #通过该方法可以找到i标签下所有的内容，以列表的形式
print(i.children)  #通过该方法可以找到i标签下所有的内容，以生成器的形式,可以遍历
for m in i.children:
    print(m)

"""
