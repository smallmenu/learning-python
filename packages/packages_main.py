import sys
import os

# 如果需要独立运行这个脚本，模块搜索路径中只包含当前脚本的目录，即：learning-python/packages 目录
# 而在这个目录下，并不存在 packages 这个包，运行会报错
dir_home = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_home, "../"))

from packages.package import Package
from packages.b.moduleb_main import PackagesModuleBMain
from funs.fun import Fun

class PackagesMain:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('PackagesMain Class Name:{0}'.format(self.name))

        # 当前目录下的其他模块
        m = Package('name')
        m.say()

        # 当前目录下的子模块
        b = PackagesModuleBMain('name')
        b.say()

        f = Fun('name')
        f.say()


# 每个模块都有一个名字，通过 __name__ 属性，可以判断模块是被导入与独立运行
if __name__ == '__main__':
    print('run by itself')
    print(sys.path)

    c = PackagesMain('name1')
    c.say()
