import json
persons=[
    {'username':'yuhaip','age':20,'hh':True,'bb':'null'},
    {'username':'张三','age':30}
]
'''

#一、将python对象转化为json对象，使用dumps函数
json_str=json.dumps(persons)
print(json_str)
#二、将json内容保存在json文件中
with open('persons.json','w') as fp:
    fp.write(json_str)

#三，利用dump函数直接进行转化并存储
with open('persons1.json','w') as fp:
    json.dump(persons,fp)
'''

#注意，在转化的过程中persons中的中文被转码成Unicode形式，如张三---\u5f20\u4e09,因为ensure_ascii参数默认为True了，会将所有字符转化成ascii码，便会对中文进行转码，若将其改成False便不会转码了，但是会出现乱码的现象，需要在打开json文件时，将编码形式进行设置即:encoding='utf-8',修改后如下：
json_str=json.dumps(persons,ensure_ascii=False)
print(json_str)

with open('persons.json','w',encoding='utf-8') as fp:
    fp.write(json_str)

with open('persons1.json','w',encoding='utf-8') as fp:
    json.dump(persons,fp,ensure_ascii=False)

"""
class Cat():
    country='china'
cat=Cat()
p=[{'username':cat}]
json.dumps(p)  
#此时会报错，因为cat并不是json所支持的数据类型，pyhton中只支持，字符串、list、tumple、int、float、布尔值，null这些数据类型转化为json形式,不是的话，需要转换成基本数据类型才能与json进行转化
"""
