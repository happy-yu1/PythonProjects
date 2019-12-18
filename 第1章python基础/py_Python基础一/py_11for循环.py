list = ['a', 'b', 'c', 'd']  # 此时为列表
i = 0
while i < 4:  # 用while循环
    print(list[i],end="")
    i = i + 1
print('-' * 40)

for i in list:  # 用for循环
    print(i,end="")

print('-'*40)
str = 'asdfgh'
for n in str:
    print(n)

m=['h','e','l','l','o']
for i in range(len(m)):
    print(m[i],end="")
