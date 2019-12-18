import re

print(re.match('[1-9]|abc', '1abc'))
print(re.match('[1-9]|abc', 'abc'))
print(re.match('[1-9]|abc', 'abc1'))

print(re.match('[1-9]$|abc', '1abcd'))

s1 = '123456@163.com'
s2 = '123456@126.com'
s3 = '123456@qq.comqqq'
print(re.match(r'\w{4,8}@(163|126|qq)\.com$', s1))
print(re.match(r'\w{4,8}@(163|126|qq)\.com$', s2))
print(re.match(r'\w{4,8}@(163|126|qq)\.com$', s3))

s4 =r'([a-z][0-9]{3})--([0-9][a-z]{3})--\1--\2$'
# t = 'a123--9asd--a123--9asd'
t = 'a123--9asd--b223--8aad'
# print(re.match(r'([a-z][0-9]{3})--\1$', 'a123--a123'))  #要加入r表示规范
# print(re.match('[a-z][0-9]{3}--[a-z][0-9]{3}$', 'a123--a123'))
l=re.match(s4,t)
print(l)
print(l.group())
print(l.group(1))
print(l.group(2))

