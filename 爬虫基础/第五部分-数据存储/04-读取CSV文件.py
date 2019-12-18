import csv

#有两种读取的方式
"""

#一、用reader()方法
with open('class.csv','r',encoding='utf-8') as fp:
    reader=csv.reader(fp)  #是一个迭代器，可通过for …… in 的方式进行迭代
    for i in reader:  #i是list类型
        print(i)
#用这种方法，会输出标题行['username', 'age', 'height', 'score']，如果不要可进行如下操作：

with open('class.csv','r',encoding='utf-8') as fp:
    reader=csv.reader(fp)
    next(reader)  #next()是迭代器中的使用，执行一次就迭代一次，将标题过滤掉
    for i in reader:
        print(i)
        
#若要获取某几个具体的信息，如获取姓名和分数，操作如下：


with open('class.csv','r',encoding='utf-8') as fp:
    reader=csv.reader(fp)
    next(reader)
    for i in reader:
        username=i[0]
        score=i[-1]  #因为是倒数第一个，下标可以是-1
        print({'username':username,'score':score})
"""
#二、用DictReader()方法
with open('class.csv','r',encoding='utf-8') as fp:
    reader=csv.DictReader(fp)  #是一个迭代器
    for i in reader:  #i是字典形式的——collections.OrderedDict
        values={'username':i['username'],'score':i['score']}
        #通过键的信息获取对应的值，实际应用中更不容易出现问题，较常用
        print(values)
#结果类似：{'username': '王7', 'score': '80'}