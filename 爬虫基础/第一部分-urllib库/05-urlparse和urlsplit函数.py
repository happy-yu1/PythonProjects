from urllib import request
from urllib import parse
url='https://timgsa.baidu.com/s;hello?wd=ABC&uername=zhang3#2'

result1=parse.urlparse(url)  #比urlsplit多了一个params属性，内容为url中 ；和？中的内容，词例中为hello

result2=parse.urlsplit(url)
print(result1)
print(result2)

#若想获得其中的某一项则,如想获得协议名：
print('scheme:',result1.scheme)