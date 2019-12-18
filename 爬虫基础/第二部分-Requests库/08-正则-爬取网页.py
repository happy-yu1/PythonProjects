import requests,re
from urllib import parse
print(re.match('12.*?hh','12hh'))

print(re.match('12.*?hh','12o9ohh'))

#爬取网页中的所有超链接
bm=parse.urlencode({'wd':'中国'})  #对中国进行编码

# 原本是这样的wd=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0，表示wd=机器学习，但此时想爬取和“中国”有关的数据，需要对“中国”进行编码后，替换掉之前的“机器学习”，并传到url中
# url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&oq=12%2526lt%253B06&rsv_pq=87b24dad003b1a8f&rsv_t=a6c7HbRo3Rr4740D%2BHQdvr2IgB1dwLYQLVoiAEzd6qQGaXKDQ2DMM6xhTTI&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=7&rsv_sug7=100&bs=12306'

url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&'+bm+'&oq=12%2526lt%253B06&rsv_pq=87b24dad003b1a8f&rsv_t=a6c7HbRo3Rr4740D%2BHQdvr2IgB1dwLYQLVoiAEzd6qQGaXKDQ2DMM6xhTTI&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=7&rsv_sug7=100&bs=12306'

header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
resp=requests.get(url,headers=header)

# print(resp.text)
regular=re.compile('<a\s+href=.*?>.*?</a>',re.S)  #匹配规则
# regular=re.compile('<a\s+href="https:.*?".*?>.*?</a>',re.S)
result=re.findall(regular,resp.text)
# print(type(result))  #是列表格式，所以可以遍历每个元素
for i in result:
    print(i)