# list = [1, 2, 3, 5, 4, 6, 5]
# i = 0
# while i < len(list):
#     if 7==list[i]:
#         print('True')
#         break
#     i += 1
# else:
#     print('游戏结束')


list = [1, 2, 3, 5, 4, 6, 5]
i = 0
while i < len(list):
    if (list[i] % 2)!=0:
        i+=1
        continue
    print(list[i])
    i+=1
else:
    print('游戏结束')