import sys

from packages.a.modulea import ModuleA
from packages.package import Package


class PackagesModuleBMain:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('packages/b/moduleb_main.PackagesModuleBMain Class Name:{0}'.format(self.name))

        m = ModuleA('a.name')
        m.say()

        p = Package('b.name')
        p.say()


# 每个模块都有一个名字，通过 __name__ 属性，可以判断模块是被导入与独立运行
if __name__ == '__main__':
    print(sys.path)
    c = PackagesModuleBMain('b.name')
    c.say()
