#百度百科刘德华，访问这个网页
from urllib import request
from urllib import parse
#'''先在百度上搜索刘德华，将网址复制下来：https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=刘德华，此时，里面是包含汉子：wd=刘德华'''

# 错误示范
# url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu'
# req=request.urlopen(url)
# # print(req.read())   会报错，需要对刘德华进行编码
# qs={'wd':'刘德华'}
# code=parse.urlencode(qs)

# 正确操作
url='https://www.baidu.com/s'
params={'wd':'刘德华'}
qs=parse.urlencode(params) #进行编码
url=url+'&'+qs  #将进行编码后的刘德华带入url中，以便识别
req=request.urlopen(url)#打开网页
print(req.read())  #读取网页源代码