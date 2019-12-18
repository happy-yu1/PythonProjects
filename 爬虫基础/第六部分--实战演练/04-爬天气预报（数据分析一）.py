#提取出前10个气温最低的城市
#思路：先将获得的最低气温进行排序————

#进行小测试 ，气温必须是数值型的，字符串的不可以，需要转成数值型的再进行排序
All_Date=[{'city': '北京', 'low_temp': -3}, {'city': '海淀', 'low_temp': -5}, {'city': '朝阳', 'low_temp': -4}, {'city': '顺义', 'low_temp': 1}, {'city': '怀柔', 'low_temp': -6}, {'city': '通州', 'low_temp': 0}]

#法一：
# def func(date):
#     low_temp=date['low_temp']
#     return low_temp
# All_Date.sort(key=func)   #sort方法默认是从小往大进行排序,key为筛选规则

#测试lambda方法
#def方法可以使用lambda 创建匿名函数的方式进行书写如：
# c=lambda a,b:a+b  #a,b为要传入的参数，：后的是要返回的值
# print(c(1,2))  ————3

#法二：
All_Date.sort(key=lambda date:date['low_temp'])
print(All_Date)

#key=func的作用是传入一个函数，按照函数返回的值，即按照城市温度进行排序
#因为All_Date变量是一个列表，可以进行排序，但是列表中的元素是一个个字典，想以字典里面的'low_temp'对应的值为依据，进行排序，所以需要通过传入函数的方式，func（date）函数即为所需。其中date为All_Date中的一个个列表
#sort函数会遍历All_Date中的每一个元素（即一个个字典），将元素传到func（）函数中去，
