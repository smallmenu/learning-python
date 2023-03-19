import sys

from packages.a.modulea  import ModuleA
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