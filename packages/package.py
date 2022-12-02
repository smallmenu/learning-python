class Package:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('packages/package.Package Class Name:{0}'.format(self.name))