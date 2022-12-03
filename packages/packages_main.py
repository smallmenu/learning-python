import sys

from packages.package import Package
from packages.b.moduleb_main import PackagesModuleBMain


class PackagesMain:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('PackagesMain Class Name:{0}'.format(self.name))

        # # 当前目录下的模块
        m = Package('name')
        m.say()

        b = PackagesModuleBMain('name')
        b.say()


# 每个模块都有一个名字，通过 __name__ 属性，可以判断模块是被导入与独立运行
if __name__ == '__main__':
    print('run by itself')
    print(sys.path)
    c = PackagesMain('name1')
    c.say()
