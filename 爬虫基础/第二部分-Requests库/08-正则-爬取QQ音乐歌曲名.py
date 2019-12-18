import requests,re
from urllib import parse

#<a href="https://y.qq.com/n/yqq/song/002Mtxzu1oQecJ.html" class="js_song" title="I Adore You ">I Adore You</a>
#<a href="https://y.qq.com/n/yqq/song/000a2bMl33mXkU.html" class="js_song" title="悬溺 ">悬溺</a>
#爬取网页中的所有超链接
url='https://y.qq.com/n/yqq/toplist/4.html'

header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36','Referer':'https://y.qq.com/n/yqq/toplist/4.html','cookie': 'pgv_pvid=4234318893; yqq_stat=0; pgv_pvi=9323009024; pgv_si=s9366849536; pgv_info=ssid=s3611619953; ts_uid=4279460712; userAction=1; ts_last=y.qq.com/n/yqq/toplist/4.html; _qpsvr_localtk=0.2190360363317334; wxuin=o1152921504967565976; qm_keyst=C9773FBD31B5B03E90AD9E95F53DC5E475B83DE53E2E55E24948CE1B0AA34326; wxopenid=opCFJw0XF4zaP1QBA-7s6WLZLG1Q;wxrefresh_token=26_XnrZwgJU7mS-5eGZfafdQixeZs_ckE5sABjzGKsZVTvrEcmJlsn7v5iP1eSs6RHmd877qq-6HXqDffDupDQxSg; wxunionid=oqFLxskFPfUxrM7ycz7e70h0hOus; login_type=2'}
resp=requests.get(url,headers=header)

regular=re.compile('<a\s+href=".*?"\s+class="js_song"\s+title="(.*?)">.*',re.S)  #匹配规则
print(resp.text)   #获取不了歌曲信息，依旧是登录界面的信息
# result=re.findall(regular,resp.text)
# print(result)
# print(type(result))
# for i in result:
#     print(i)