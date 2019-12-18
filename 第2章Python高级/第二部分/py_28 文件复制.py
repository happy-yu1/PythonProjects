# 小文件复制
# file_read = open('F:/a.txt')  # 默认以只读方式打开已存在的 a.txt
# file_write = open('F:/b.txt', 'w')  # 以只写方式打开 即复制的 b.txt
#
# text = file_read.read()
# file_write.write(text)  # 执行后便创建了b.txt


# 复制大文件，可将读和写分别放在不同的函数里，通过调用函数实现复制
# 复制时可以按行或者字节进行复制

def read_file():  #错误了？
    file_read1 = open('F:/a.txt')
    global f1
    while True:
        f1 = file_read1.read(4)
        if not f1:
            break
        else:
            print(f1)

def write_file():
    file_write1=open('F:/f.txt','w')
    print('_____2____')
    file_write1.write(f1)
    print(f1)
    print('_____3____')
if __name__ == '__main__':
    read_file()
    write_file()
