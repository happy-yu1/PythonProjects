# dict = {1930: '巴西', 1931: '中国', 1932: '巴西', 1933: '美国'}
# team = input('请输入国家：')
# for year in dict:
#     if team == dict[year]:
#         print('%d' % year, end=' ')
# else:
#     print('没有获奖')

b='zxc'
def a():
    global b
    b='qwe'
a()
print(b)
