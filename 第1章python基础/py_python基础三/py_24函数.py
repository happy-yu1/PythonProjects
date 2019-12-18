def num(a,b):
    if a>b:
        print(a)
    else:
        print(b)

a=10
b=30
num(a,b)

def num1(a):
    print('aaa')
def num1(a,b):    #  当同一个文件下两个函数名一样时，会调用最后一个，前面一样的会被覆盖
    print('bbb')

num1(3,4)  # 此时执行的是第二个，如果num1（3）会显示错误


def num2():  # 无参函数，下次出现时直接会显示print中的内容
    print('hello python')
num2()
