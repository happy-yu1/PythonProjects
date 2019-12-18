#安装 pip install bs4（或beautifulsoup4）
from typing import Iterable


from bs4 import BeautifulSoup
import requests

url='https://zhidao.baidu.com/question/246019942011070764.html'
res=requests.get(url)
html=res.content.decode('gbk')
soup=BeautifulSoup(html,'lxml')
"""
<div class="wgt-header-title-content" style="display: block;">
    <h1 class="wgt-header-title-text">pycharm运行代码快捷键是哪个</h1>
    <span class="iknow-icons wgt-header-title-btn"> 我来答</span>
    <span class="exp-topwld-tip">新人答题领红包
        <a class="exp-topwld-tip-close"></a></span>
</div>

# a=soup.select('div.wgt-header-title-content')
#挑选class="wgt-header-title-content"的div
# a=soup.select('div.wgt-header-title-content')

#挑选class属性包含‘wgt’的h1标签
# a=soup.select('h1[class*=wgt]')

#先挑选class属性包含‘wgt’的div标签 ，再从中挑选出子元素h1标签,只筛选子元素
# a=soup.select('div[class*=wgt] > h1')
a=soup.select('div[class*=wgt] a')
print(a)
"""

"""
#先挑选class属性包含‘tain’的header标签 ，再从中挑选出所有ul标签,载从ul中挑选所有的li标签，不仅仅是选子元素
a=soup.select('header[class*="tain"] ul li')   #list类型，里面包含多个li标签
# print(type(a),len(a),a,sep='\n')
for i in a:  #i是Tag类型
    print(i.string)  #获得每个li标签中的文本
"""
a=soup.select('#container .adTopImg from-fyb')
print(a)
"""
<header id="header" class="container">
    <a log="page:question,action:click,pos:fyb-word" href="https://www.baidu.com/baidu?rsv_dl=fyb_n_zhidaoqb&amp;word=不再公布楼市均价" target="_blank" class="adTopImg from-fyb" style="left: 894.5px; display: none;">不再公布楼市均价</a>

    <div id="search-box" class="search-box-new line">
        <ul class="channel grid">
            <li><a log="sc_pos:c_baidu" data-type="baidu" rel="nofollow" href="http://www.baidu.com/">网页</a></li>
            <li><a log="sc_pos:c_news" data-type="news" rel="nofollow" href="https://www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;fr=zhidao">资讯</a></li>
            <li><a log="sc_pos:c_video" data-type="video" rel="nofollow" href="https://www.baidu.com/sf/vsearch?pd=video&amp;tn=vsearch&amp;wd=&amp;rsv_spt=16">视频</a></li>
            <li><a log="sc_pos:c_pic" data-type="image" rel="nofollow" href="http://image.baidu.com/">图片</a></li>
            <li><strong>知道</strong></li>
            <li><a log="sc_pos:c_doc" data-type="wenku" rel="nofollow" href="http://wenku.baidu.com/">文库</a></li>
            <li><a log="sc_pos:c_tieba" data-type="tieba" rel="nofollow" href="http://tieba.baidu.com/">贴吧</a></li><li><a log="sc_pos:c_b2b" data-type="b2b" rel="nofollow" href="https://b2b.baidu.com/">采购</a></li>
            <li><a log="sc_pos:c_map" data-type="map" rel="nofollow" href="http://map.baidu.com/">地图</a></li><li><a log="sc_pos:c_more" data-type="more" href="http://www.baidu.com/more/">更多»</a></li>
        </ul>
    <div class="search-block clearfix under-shadow" mark="on" style="display: none;">
        <div class="search-cont clearfix">
         <a class="logo" href="/" title="百度知道"></a>
<form action="/search" name="search-form" method="get" id="search-form-new" class="search-form">
<input class="hdi" id="kw" maxlength="256" tabindex="1" size="46" name="word" value="" autocomplete="off" placeholder="">
<button alog-action="g-search-anwser" type="submit" id="search-btn" hidefocus="true" tabindex="2" class="btn-global">搜索答案</button>
<a href="#" alog-action="g-i-ask" class="i-ask-link" id="ask-btn-new">我要提问</a>
</form>
</div>
</div>
</div>
<script>
                    // 搜索框可用时间打点
                    alog && alog('speed.set', 'c_sbox', +new Date); alog.fire && alog.fire("mark");
                </script>

<div class="wgt-header-title wgt-header-title-shadow">
<div class="wgt-header-title-content" style="display: block;">
<h1 class="wgt-header-title-text">pycharm运行代码快捷键是哪个</h1>
<span class="iknow-icons wgt-header-title-btn"> 我来答</span><span class="exp-topwld-tip">新人答题领红包<a class="exp-topwld-tip-close"></a></span>
</div>
</div>

</header>
"""



