# encoding:utf-8
from urllib import parse
date={'name':'爬','greed':'hello world','age':100}
qs=parse.urlencode(date)
print(qs.split('&'))
print(qs)

qs2='name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greed=hello+world&age=100'
print(parse.parse_qs(qs2))