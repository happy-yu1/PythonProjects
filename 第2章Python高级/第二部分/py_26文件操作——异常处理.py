def read_file1():
    try:  # 文件打开和读取的过程均会发生错误，如文件不存在会抛出异常
        f = None  # '''如果运行（打开或者读取出错，f将不会被赋值，即不存在f，
        # 后期调用会报错，所有需要先将f进行赋值
        f = open('F:/a.txt', 'r')
        text = f.read()
        print(text)
    except Exception:
        print('_____1______')
        print('发生异常')
    finally:    # 无论是否发生异常，均要关闭文件，借用finally
        if f is None:
            pass
        else:
            f.close()



def read_file2():
    try:
        # f=None
        # f = open('F:/a.txt', 'r')
        with open('F:/a.txt', 'r') as f:
            print(f.read())
# '''使用with语句后，不需要再单独编写finally语句进行文件的关闭，也不用提前对f进行赋值
    # 1、2两种方法均可以实现异常处理和文件的关闭
    except Exception:
        print('_____2______')




if __name__ == '__main__':
    read_file1()
    # write_file()
    read_file2()
