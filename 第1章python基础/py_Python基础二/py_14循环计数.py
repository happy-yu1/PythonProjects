# i=1  # 输出1~100内的奇数
# while i<=100:
#     print(i)
#     i+=2

i=0    # 另一种方法输出1~100内的奇数
# while i<=100:
#     if (i % 2)==0:
#         i+=1
#         continue
#     print(i)
#     i+=1
for i in range(10):
    print(i,end=" ")

print( )

for i in range(10,20):
        print(i, end=" ")
print( )

i=list(range(10))
print(i)

i=list(range(1,10,2))  # 输出包含1~n之间的奇数的列表
print(i)

n=int(input('请输入：'))  # 输出包含1~n之间的奇数的列表
i=list(range(1,n,2))
print(i)