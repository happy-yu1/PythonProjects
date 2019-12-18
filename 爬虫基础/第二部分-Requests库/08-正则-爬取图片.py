import requests,re
from urllib import parse,request

#一、根据规则1获取妹子网页的相关图片链接
url='https://www.douban.com/photos/album/1647622767'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
resp=requests.get(url,headers=header)
print(resp.text)
# regular1=re.compile('<img\s+width="201"\s+src=.*?>',re.S)
# result=re.findall(regular1,resp.text)
# print(type(result))
# for i in result:
#     print(i)
    # print(type(i))  #为str类型,而非list，，为什么？，若是list可用i[n]的方式调取对应的结果，并将其命名，方便做信息提取
#二、根据规则2，在一的基础上进一步将链接筛选出来，使用sub（）方法
'''regular2=re.compile('<img width="201" src="|" />.*')
for s in result:
    img=re.sub(regular2,'',s)
    print(img)
# print(type(result))  ----list形式
# print(len(result)) -----共有4张图
'''
#三、将获得的超链接放到一个list中
# regular2=re.compile('<img width="201" src="|" />.*')
# imglist=[]
#
# for i in result:
#     img = re.sub(regular2,'',i)
#     # print(type(img))  -----str
#     imglist.append(img)
# print(imglist)

#四、将imglist中的链接分别以img文件的形式保存下来
#法一：
'''for i in range(len(imglist)):
    imgname = '%d.jpg' % i
    resp=requests.get(imglist[i],headers=header)
    with open (imgname,'wb') as f:
        f.write(resp.content)  #必须要用content，因网路间传输用二进制
'''
#法二：
# for i in range(len(imglist)):
#     imgname = '%d.jpg' % i
#     request.urlretrieve(imglist[i],imgname)