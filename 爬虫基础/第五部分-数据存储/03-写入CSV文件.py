import csv


"""
#一、将Python对象写入到CSV文件中————法一（元组的形式）
header=['username','age','height','score']  #输入标题信息，可以是list也可以是tuple类型的
values=[('张三',19,170,99),  #传入每个具体的详细数据
        ('李四',20,175,100),
        ('王1',42,170,70),
        ('王2',32,181,88),
        ('王3',21,150,56),
        ('王4',25,180,43),
        ('王5',28,183,89),
        ('王6',42,184,76),
        ('王7',56,180,80)
        ]

with open('class.csv','w') as fp:
    writer=csv.writer(fp,delimiter=';') 
#若想修改列和列之间的分隔符，可修改delimiter参数，默认的是“，” 若将其设置成delimiter=';'，则用分号进行分割
    writer.writerow(header) #传入标题信息，只传一行
    writer.writerows(values) #传入具体的数据，多行信息

结果如下：存在乱码，而且每行信息间有一个空格，可以进行调整
username,age,height

����,19,170

����,20,175

����,22,180

with open('class.csv','w',encoding='utf-8',newline='') as fp:
    writer=csv.writer(fp)
    writer.writerow(header) #传入标题信息，只传一行
    writer.writerows(values) #传入具体的数据，多行信息
"""
#二、写入到CSV文件中————法二 （以字典的形式）
header=['username','age','height','score']
#以字典的形式将具体的信息传入进去
values=[{'username':'张三','age':19,'height':170,'score':99},
       {'username':'李四','age':20,'height':130,'score':89},
        {'username':'王1','age':19,'height':170,'score':99}]

with open('class1.csv','w',encoding='utf-8',newline='') as fp:
    writer=csv.DictWriter(fp,header) #需要同时传入两个参数，文件和题目
    writer.writeheader()  #写入题目
    # writer.writerow(header)  这种方法不可传入题目，必须用writeheader()方法
    writer.writerows(values)