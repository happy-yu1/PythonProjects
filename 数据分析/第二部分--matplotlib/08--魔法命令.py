from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager

# a=np.arange(12).reshape(3,4)
# plt.imshow(a,cmap='bone',interpolation='nearest',origin='upper')


# x = range(1, 32)
# y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
#        22, 23]
# plt.figure(figsize=(20, 8), dpi=90)
# plt.scatter(x, y_3)
# plt.show()


def func(i):
    if 8 <= i < 12:
        print('morning')
    elif 12 <= i < 18:
        print('afternoon')
        import pdb   #插入一个断点
        pdb.set_trace()
    elif 18 <= i < 24:
        print('evening')
    else:
        raise Exception('表达错误')
func(14)

