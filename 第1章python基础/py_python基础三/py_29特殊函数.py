c=lambda a,b:a+b  # 匿名函数
print(c(1,2))
print('-'*40)
# 函数的嵌套
def m1(a):
    print(a)

def m2(b):    # 先执行m2，后执行m1
    print(b)
    m1(123)
m2(456)
print('-'*40)

# 递归函数（计算1+2+3+……+n）
def sum(n):
    if n==1:  # if语句为终止条件，满足即返回进行迭退
        return 1
    else:
        return n+sum(n-1)
print(sum(100))


