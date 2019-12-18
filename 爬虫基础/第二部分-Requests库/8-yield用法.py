import json,requests,re,time



def call(i):
    return i * 2

# def yield_test(n):
#     for i in range(n):
#         yield call(i)
#         print("n=", i)
#         # 做一些其它的事情
#     print("do something.")
#     print("end.")


#yield()创建生成器后，调用时每遇到yield便中止，输出结果；下次调用时会从上次中断的地方接着运行，遇到yield后执行，再中止。
# x=yield_test(5)
# print(next(x))  #0  此时i=0，只执行 yield call(0) ，遇到生成器后就会输出结果，后面的先暂停
# print(next(x))  #n=0  2  接上一步，先执行i=0时的print("i=", 0)，再执行i=1时的yield call(1)
# print(next(x))  #n=1  4 先执行print("i=", 1)，再执行yield call(2)
# print(next(x))  #n=2  6
# print(next(x))  #n=3  8
# print(next(x))  #报错，迭代完了
# 使用for循环
# for i in yield_test(5):
#     print('m,',i)
#     # print('hello')


result=[['a','1'],['b','2'],['c','3']]
def func():
    for i in result:
        yield{'name':i[0],'age':i[1]}
for i in func():
    print(i)
