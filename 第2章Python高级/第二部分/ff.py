file_read = open('F:/a.txt')
file_write = open('F:/e.txt', 'w')
while True:
    text = file_read.read(4)
    # print(text)
    if not text: #当text为空时，结束无限循环
        break
    else:
        file_write.write(text)


