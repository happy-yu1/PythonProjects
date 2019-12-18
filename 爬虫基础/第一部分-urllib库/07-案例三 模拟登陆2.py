
from urllib import request,parse

from urllib.request import build_opener,ProxyHandler


#要访问的人人子页面信息，以大鹏网页为例：http://www.renren.com/880151247/profile
#人人网登录的主页：http://www.renren.com/

'''
#一、不用cookie时访问大鹏主页
dapeng_url='http://www.renren.com/880151247/profile'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
req=request.Request(url=dapeng_url,headers=header)
resp=request.urlopen(req)
# print(resp.read().decode('utf-8'))
#此时输出的结果并不是大鹏的主页，里面有“注册”字样，很可能是一个登录界面，可通过如下方法检查
with open('renren.html','w') as f:
    f.write(resp.read().decode('utf-8'))
'''


#二、使用大鹏个人主页下的cookie信息，添加在headers中
dapeng_url='http://www.renren.com/880151247/profile'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36','Cookie':'anonymid=k238xme8w7a75u; depovince=GW; _r01_=1; ick_login=1da23c7b-4b64-4b69-9203-fdd2960a6765; JSESSIONID=A5341AB4D209A2E73D565DAD7B84ADBA; Hm_lvt_1e59e639119e3bf348b864db2b258c57=1571833285; Hm_lpvt_1e59e639119e3bf348b864db2b258c57=1571833285; Hm_lvt_4397070d9365caef87e72dc468269464=1571833286; Hm_lpvt_4397070d9365caef87e72dc468269464=1571833286; __tins__14669305=%7B%22sid%22%3A%201571833285538%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201571835085538%7D; __51cke__=; __51laig__=1; XNESSESSIONID=abcMMrq6Jn1Lg5-6qK43w; ick=22d3c2cb-b9e2-4bfd-9da2-9020e39dc408; __utma=151146938.2033711913.1571833355.1571833355.1571833355.1; __utmc=151146938; __utmz=151146938.1571833355.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; t=a55a41165b068041876477af739412652; societyguester=a55a41165b068041876477af739412652; id=972544662; jebecookies=f0bcd2dd-c6b0-436e-a4f7-5302a5f63e47|||||; ver=7.0; jebe_key=fffff7c6-a159-456c-944d-1624e58ccddd%7Cda6f15a8c8d3f7061f2107bb848fe242%7C1571833570961%7C1%7C1571833575178; wp_fold=0; _de=5E3412B7274365E7253C8D129BFBF8EE; p=282a0b2d4b0bc54d56d547d640a1144e2; first_login_flag=1; ln_uact=17320063569; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; xnsid=7668942; loginfrom=null; Hm_lvt_416c770ac83a9d996d7b3793f8c4994d=1571833430,1571833444,1571833554,1571833900; Hm_lpvt_416c770ac83a9d996d7b3793f8c4994d=1571834376'}
req=request.Request(url=dapeng_url,headers=header)
resp=request.urlopen(req)
# with open('renren-cookie.html','w') as f:
#     f.write(resp.read().decode('utf-8'))
print(resp.read().decode('utf-8'))