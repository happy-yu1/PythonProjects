import re

# 实例一：匹配出4~8位的密码，可英文、数字、下划线

print(re.match('[\w]{4,8}', 'ahgk_lgjdlk').group())  # 不加$符，部分超过8位数的的字符串也认为匹配成功
print(re.match('[\w]{4,8}$', 'ahgk_lgjdlk'))  # 加$符，部分超过8位数的的字符串无法匹配成功

# 实例二：第一个字符不能为数字
print(re.match('[\D][\w]*', 'a1').group())

# 实例三：匹配0~99之间的数字
print(re.match('[1-9]?[0-9]', '3').group())
print(re.match('[1-9]?[\d]', '44').group())
print(re.match('[1-9]?[\d]$', '466'))  # 匹配错误

# 实例四：匹配163邮箱（要求：@163前有4~8个字符）
print(re.match('[\w]{4,8}@163\.com', '12345@163.com778').group())
print(re.match('[\w]{4,8}@163\\.com', '12345@163.com778').group())
print(re.match(r'[\w]{4,8}@163\.com', '12345@163.com778').group())  # 最规范的书写方式
print(re.match(r'[\w]{4,8}@163\.com$', '12345@163.com778'))  # 加了$符号，匹配失败
print(re.match(r'[\w]{4,8}@163\.com$', '12345@163.com').group())

# 实例五：匹配任意以下划线开头的字符串
print(re.match('_[\w]*', '_').group())
print(re.match('_[\w]*', '_1').group())
print(re.match('_[\w]*', '_1a').group())
