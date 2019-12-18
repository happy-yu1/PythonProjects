#  计算1~100的和

# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print("1~100的和为: %d" % sum)


#  计算1~n之间的和，n可以自己输入
sum = 0
i = 1
n=int(input('请输入：'))
while i <= n:
    sum = sum + i
    i += 1
print("1~%d的和为: %d" % (n,sum))