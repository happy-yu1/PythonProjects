f = open('F:/a.txt', 'r')
text1 = f.read()  # 读取所有的内容
text2 = f.read(4)  #从左往右，每4个的读取，执行一次读取4个
text3 = f.readline()  # 按行进行读取

print(text1)
print(text2)  # ?
print(text3)  # ?
