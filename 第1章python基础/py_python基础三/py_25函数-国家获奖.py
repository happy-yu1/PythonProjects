# 已知几个国家不同年份的获奖情况，输入年份，寻找该年哪个国家获奖
# dict = {1930: '巴西', 1931: '中国', 1932: '巴西', 1933: '美国'}
# year = int(input('请输入年份：'))
# if year in dict:
#     print('%d年获奖的国家是：%s' % (year, dict[year]))
# else:
#     print('没有获奖')

# 输入国家名，寻找该国是否获奖，哪几年获奖
dict = {1930: '巴西', 1931: '中国', 1932: '巴西', 1933: '美国'}
team=input('请输入国家：')
f=True  # 比较重要的，一定要设置
for i in dict:
    if team==dict[i]:
        print('%d'% i,end=" ")
        f=False  # 比较重要的，一定要设置
else:
    if f:
        print('没有获奖')
