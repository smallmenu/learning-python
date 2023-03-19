import sys
import os

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

        f = Fun('fun-name')
        f.say()