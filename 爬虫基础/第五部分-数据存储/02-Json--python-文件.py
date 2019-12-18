import json
#将json字符串转换成pyhton对象
"""
#法一：load函数
with open('persons.json','r',encoding='utf-8') as f:
    json_str=json.load(f)
    print(json_str)
"""

#法二：使用loads方法
json_str='[{"username": "yuhaip", "age": 20, "hh": true, "bb": "null"}, {"username": "张三", "age": 30}]'
# json_str=[{"username": "yuhaip", "age": 20, "hh": true, "bb": "null"}, {"username": "张三", "age": 30}]
person=json.loads(json_str)
print(person)