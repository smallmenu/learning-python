import sys
from packages.packages_main import PackagesMain


class Module1:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('Module1 Class Name:{0}'.format(self.name))


class Module2:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('Module2 Class Name:{0}'.format(self.name))


# 每个模块都有一个名字，通过 __name__ 属性，可以判断模块是被导入或独立运行
if __name__ == '__main__':
    print('run by itself')
    print(sys.path)

    # __init__.py 定义包, 默认可以直接引用同级和下级
    c4 = PackagesMain('name')
    c4.say()
else:
    print('imported from another module')
