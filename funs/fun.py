from packages.a.modulea  import ModuleA

class Fun:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('funs/Fun Class Name:{0}'.format(self.name))

        m = ModuleA('a.name')
        m.say()