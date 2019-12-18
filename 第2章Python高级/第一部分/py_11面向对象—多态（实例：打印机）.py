class Word:
    def __init__(self, filename):
        self.filename = filename  # 文件需要从外界导入
        self.text = None  # 假设为新建的文件，里面还没有内容

    def edit_text(self, t):  # 文档有编辑的功能、动作
        self.text = t  # 为文本添加内容：t

    def print_text(self, printer):  # '''体现了多态的思想，只要x类含有output_text(A)方法，
        # x类创建的对象便可接收print—_text()的信号，便出现鸭子类型'''
        printer.output_text(self.text)


class Printer:
    def __init__(self, model):
        self.model = model

    def output_text(self, content):  # 打印机打印文本中的内容
        pass  # 该内容可以不用写，因为子类会重写


class WBprinter(Printer):
    def __init__(self, model):
        super().__init__(model)

    def output_text(self, content):  # 父类方法的重写
        print('%s打印机，打印了黑白文档：%s' % (self.model, content))

if __name__ == '__main__':
    w=Word('file1')
    w.edit_text('我爱谢伟')
    p=WBprinter('sdoo3')

    w.print_text(p)
