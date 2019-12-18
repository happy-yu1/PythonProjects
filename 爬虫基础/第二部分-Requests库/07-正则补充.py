import requests,re
from urllib import parse
'''
print(re.match('12.*?hh','12hh'))

print(re.match('12.*?hh','12o9ohh'))

print(re.match('[^123]','1abc'))  #匹配不包括[]中的字符

#匹配中文字符的正则表达式： [\u4e00-\u9fa5]
#匹配双字节字符(包括汉字在内)：[^\x00-\xff]
str='中国我爱你'
print(re.match('中[\u4e00-\u9fa5]',str))

str='hello 12334 world amn'
str1='hello 12334 world amn oo'
t=re.match('he.*ld\samn$',str1)
print(t)
'''
str='''hello 123
world'''
reg='he.*?\d{3}.*?d$'
t=re.match(reg,str,re.S)
print(t)