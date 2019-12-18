def func(n):
    def func_in(n_in):
        print('func_in is %d'% n_in)
        return n+n_in
    return func_in
a=func(20)
print(a(100))
print('-'*40)
print(func(20)(100))
print('-'*40)



a=20
def func():
    a=30
func()
print(a)
print('-'*40)


b=40
def func():
    b=50
    print(b)
func()
print(b)
print('-'*40)


c=70
def func():
    c=80
func()
print(c)
print('-'*40)


c=70
def func():
    global c
    c=80
func()
print(c)