
for n in range(3,100):
    for i in range(2,n):
        if (n%i)==0:
            break
    else:
        print('%d'% n,end=" ")

# i = 2
#
# for n in range(3,100):
#     while i<n:
#         if (n%i)==0:
#             break
#         i+=1
#     else:
#         print("%d" % n, end=' ')





