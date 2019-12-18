# encoding:utf-8
from urllib import request
# resp=request.urlopen('https://www.baidu.com')
# # print(resp.getcode())
request.urlretrieve('http://www.baidu.com','baidu.html')
request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571651459608&di=57b811e426e2cfab80c300d31735d357&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fq_70%2Cc_zoom%2Cw_640%2Fupload%2F20170221%2Fc562deb6d0424c5389ea198ca69d3346_th.jpeg','luxun.jpg')