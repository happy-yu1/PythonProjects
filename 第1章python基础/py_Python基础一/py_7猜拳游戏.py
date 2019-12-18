

import random
p = int(input('请出拳（1：石头，2：剪刀，3：布）：'))
# c = 1  # 假设电脑只会出1
c = random.randint(1, 3)  # 对c进行使用随机方法，随机选取1-3中的任意整数
if (p == 1 and c == 1)\
    or (p == 2 and c == 2) \
       or (p == 3 and c == 3):
    print("平局")
elif (p == 1 and c == 2) \
        or (p == 2 and c == 3) \
        or (p == 3 and c == 1):
    print("赢了")
elif (p == 1 and c == 3) \
        or (p == 2 and c == 1) \
        or (p == 3 and c == 2):
    print("输了")
