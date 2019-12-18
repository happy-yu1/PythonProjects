import timeit

def func():
    list=[]
    for i in range(1000):
        list.append(i)
   

l=[i for i in range(1000)]

print(type([i for i in range(1000)]))

# t1=timeit.timeit(stmt=func(),number=1000)

t1=timeit.timeit(stmt=func,number=10000)
# t2=timeit.timeit(stmt=str(l),number=10000)
t2=timeit.timeit(stmt='[i for i in range(1000)]',number=10000)
print(t1)
print(t2)
# c='''
def func2(num):
    for i in range(num):
        print ('Repeat for {}'.format(i))
# '''

t3=timeit.timeit('func2(num)',setup=func2+'num=3',number=10)
print(t3)