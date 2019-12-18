def read_file():  # 只读
    f = open('F:/a.txt', 'r')
    text = f.read()
    print(text)
    f.close()  # 无论是否报错均要关闭文件


def write_file():  # 只写
    f = open('F:/a.txt', 'w')
    text = 'love xie'  # 后面必须为字符串
    f.write(text)
    f.close()


def add_file():
    f = open('F:/a.txt', 'a')
    text = 'little baby little baby little baby little baby'
    f.write(text)
    f.close()


if __name__ == '__main__':
    # read_file()
    write_file()
    add_file()
    read_file()
