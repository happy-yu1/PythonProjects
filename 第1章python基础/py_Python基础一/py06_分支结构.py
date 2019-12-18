# x = int(input('请输入年份：'))
# if x % 4 == 0 and x % 100 == 0 or x % 400 == 0:
#       # print('%d是闰年' % x)
# else:
#     print('%d是平年' % x)

a = float(input('您的体重是：'))
b = float(input('您的身高是：'))
bmi = a / b ** 2
print(bmi)
if bmi < 18.5:
    print('您的身高是%fm，体重是%fkg，偏轻' % (b, a))
elif 18.5 <= bmi < 25:
    print('您的身高是%fm，体重是%fkg，正常' % (b, a))
elif 25 <= bmi < 28:
    print('您的身高是%fm，体重是%fkg，微胖' % (b, a))
else:
    print('您的身高是%fm，体重是%fkg，超胖' % (b, a))
