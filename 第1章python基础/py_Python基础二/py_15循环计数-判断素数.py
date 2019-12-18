# n = int(input('请输入：'))
# i = 2
# while i < n:
#     if ( n%i ) == 0:
#         print('%d不是素数' % n)
#         break
#     i+=1
# else:
#     print('%d是素数' % n)


n = int(input('请输入：'))    # 用for in 函数判断n是否为素数
for i in range(2,n):
    if ( n%i ) == 0:
        print('%d不是素数' % n)
        break
else:
    print('%d是素数' % n)
