s1={1,2,3,4}
s2={}  # 此时为字典类型
s3={()}  # 此时为正确空集合的写法
print(type(s1))
print(type(s2))
print('*'*20)
print(type(s3))

s4=(1)
s5=(1,)
print(type(s4))
print('*'*20)
print(type(s5))

s6={1,1,2,2,3,4}  # 集合的不可重复性
print(s6)


print('-'*40)
s1={1,2,3,4}
s7={1,5,6,4,7}
print(s1-s7)  # 差
print(s1|s7)  # 并
print(s1 & s7)  # 交
print(s1 ^ s7)  # 不同时存在于二者之间的数，
print('-'*40)
s1.remove(2)
print(s1)

print('-'*40)
s10=s1.copy()
print(s10)
print(s1)
s1.add(10)  # 10添加的位置是不确定的
print(s10)
print(s1)