name = 'zhang3'
score = 87.5
age = 12

print("我的名字是%s, 今年%d岁, 考了%f分" % (name,age, score))    # 默认小数点保留五位
print("我的名字是%s, 今年%d岁, 考了%.1f分" % (name,age, score))   # 将分数的小数点保留一位

num = 1001
print("学号：%06d,我的名字是%s, 今年%d岁, 考了%.1f分" % (num,name,age, score))


print("%e" % 12345)   # 以科学计数法表示浮点数
print("%.2f" % 12345)   # 以浮点数表示
print("占用了%.2f%%" % 23.4)     #  表示占用了23.4%


th1 = '''qqqqqqqqq,
ffffffff,
kkkkkkkkkkk,
'''

str = "abcde"
print("字符串%s的长度是%d" % (str,len(str)))
print('abs'.upper())     # 方法表示而不是函数

sp = "-".join("qwert")
print(sp)
print("-".join("qwert"))

str = 'this is a'
a = str.split(" ")
print(a)
print(a[0])
print(a[1])
print(a[2])
