import requests
from lxml import etree
#已存在html文件时，读取文件
#因为parse（）在解析时，默认使用xml解析器，需改变适用html的解析器，防止解析时出现问题
parser=etree.HTMLParser(encoding='utf-8')
htmlelement=etree.parse('lagou.html',parser=parser) #添加parse属性
# print(type(htmlelement))  #为element对象，并不是字符串
'''
result=etree.tostring(htmlelement)
print(type(result))   #bytes格式的数据

result=etree.tostring(htmlelement,encoding='utf-8').decode('utf-8')
# print(result)

#利用xpath提取信息
#1、提取a标签,第一种模糊查询，按href属性筛选出符合要求的a标签；第二种精确查询，按class="position_link"属性进行a标签筛选
result1=htmlelement.xpath('//a[contains(@href,"https://www.lagou.com/jobs")]')
result=htmlelement.xpath('//a[@class="position_link"]')
'''
# 筛选出标签a下面href属性，href属性中的url即为职位详情
result=htmlelement.xpath('//a/@href')
'''
print(type(result))   #为list，遍历每个元素
for i in result:
    # print(type(i))  #result中的每个元素均为一个element对象，
    print(i)   #结果类似于 <Element li at 0x3623888>，是一个对象，需要进行编码和解码成Unicode数据
    '''
# for i in result:
    # print(etree.tostring(i,encoding='utf-8').decode('utf-8'))
    # print(i) #当result中的信息为url时，不需要再用encoding进行转码
title=htmlelement.xpath('//h3/text()')
print(title)

