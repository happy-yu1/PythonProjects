# price=6666
#
# while True:  # 死循环，且价格已给出
#     userprice = int(input('请出价：'))
#     if userprice<price:
#         print('低了')
#     elif userprice>price:
#         print('高了')
#     else:
#         print('中奖')
#         break    # 结束死循环


import random
price=random.randint(100,200)
while True:
    userprice = int(input('请出价：'))
    if userprice<price:
        print('低了')
    elif userprice>price:
        print('高了')
    else:
        print('中奖')
        break