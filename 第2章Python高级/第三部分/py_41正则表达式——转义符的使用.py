import re

# 若想匹配\n123,则

s = '\\n123'
print(s)  # \n123

print(re.match('\\\n123', s))   # None
print(re.match('\\\\n123', s))
print(re.match('\\\\n123', s).group())  # \n123
print(re.match(r'\\n123', s).group())  # \n123  正规书写



