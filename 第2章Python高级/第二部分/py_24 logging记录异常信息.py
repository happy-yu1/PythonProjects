import logging

logging.basicConfig(level=logging.INFO)  # 通过改变logging.__后的代码，得到想要的提示语
logger = logging.getLogger()

logger.warning('警告警告')


class Base:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func(self):
        r = None
        try:
            r = (self.x / self.y)
        except ZeroDivisionError:
            # print('除数为0')
            logger.error('除数为0')
            logger.info('---1--')

        except TypeError:
            logger.error('除数为字母')
            logger.info('----2---')
        finally:
            print(r)


class Sub(Base):

    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == '__main__':
    # s1 = Sub(4, 2)
    # s1.func()

    # print('*' * 40)
    #
    # s2 = Sub(4, 0)
    # s2.func()
    #
    # print('*' * 40)

    s3 = Sub(4, 'a')
    s3.func()
