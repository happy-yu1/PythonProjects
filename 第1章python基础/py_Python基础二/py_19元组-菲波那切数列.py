a = 1
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(1, 19):  # （1，19）里面的数字可以随意，只要二者范围内有18个数即可
    a, b = a + b, a
    print(a, end=" ")
print( )
str="1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765"
a=str.split(" ")
print(a)
print(len(a))
b=list(str)
print(b)
print(len(str))

c="asdfg"
print(len(c))
