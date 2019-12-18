import re

print(re.match('www', 'wwwg'))
print(re.match('www', 'wwwg').group())  # 输出最后匹配到的结果
print(re.match('www$', 'wwwg'))  # 匹配失败
print(re.match('www$', 'www'))  # 匹配成功



# 匹配单个字符
print(re.match('.', 'www'))  # w
print(re.match('.n', 'wnw'))  # wn
print(re.match('[0-9a-z]', '1www'))  # 1
print(re.match('[0-9a-z].', '1www'))  # 1w

# 匹配多个字符
print(re.match('[0-9a-z]*', '1www'))  # 1www
print(re.match('[0-9a-z]+', '1www'))  # 1www
print(re.match('[0-9a-z]?', '1www'))  # 1
print(re.match('[0-9a-z]*', 'Wwww'))  # 特别：此时匹配值为空，不是None
print(re.match('[0-9a-z]*', 'Wwww').group())
print(re.match('[0-9a-z]{2,5}', 'www'))  # www
print(re.match('[0-9][a-z]', '1www'))  # 1w

print(re.match('a', 'awww'))  # a
print(re.match('[a]', 'awww'))  # a

print(re.match('\w', 'awww'))  # a
print(re.match('a[\w]', 'awww').group())  # aw


print(re.match('^w', 'www'))
print(re.match('[^w]', 'www'))  # [^w]表示排除
print(re.match('[^w]', 'awww'))