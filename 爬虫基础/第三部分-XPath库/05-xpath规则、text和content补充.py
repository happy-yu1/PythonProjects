from lxml import etree
import requests


# a='hhhh'
# b=[]
# # b=[a]
# b.append(a)
# print(b)

str1='''
<div class="a" data-isnew="false" data-id="26709258"></div>
<div class ="b" data-isnew="false" data-id="26709258" ></div>
<div class ="c" data-isnew="false" data-id="26709258" ></div>
<div class ="d" data-isnew="false" data-id="26709258" ></div>
'''
# html=etree.HTML(str1)
# detail_url1=html.xpath('//div[2]/@class')  #正数第二个
# detail_url2=html.xpath('//div[position()<3]/@class')
# detail_url3=html.xpath('//div[last()]/@class')  #倒数第一个
# detail_url=html.xpath('//div[last()-1]/@class')  #倒数第二个
# print(detail_url)
Header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
url1 = 'https://www.ygdy8.net/html/gndy/dyzz/index.html'
resp = requests.get(url1)
text1 = resp.text  #返回的是字符串

# 此时出现中文乱码了，因为响应头中content-type: text/html，而没有对服务器返回的响应头进行特定形式的编码，需要进行如下操作:法一
# t=bytes(text1,encoding='iso-8859-1')  #将字符串按之指定的编码形式转换成bytes类型的数据
# s=str(t,encoding='gbk')   #将编码后的数据按指定的编码形式转码成字符串,可用gbk或utf-8
# print(s)

#法二：不用text 而用content
text1 = resp.content.decode('gbk')
print(text1)  #结果不会出现中文乱码


# url2='https://maoyan.com/films/1203'
# resp = requests.get(url2,headers=Header)
# text2 = resp.text
# print(text2)
# 此时中文没有乱码了，因为响应头中content-type: text/html后有charset=utf-8，对服务器返回的响应头以utf-8的编码形式进行编码