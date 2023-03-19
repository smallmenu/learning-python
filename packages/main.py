import sys
import os

# 如果需要独立运行位于子模块下的脚本，模块搜索路径中只包含当前脚本的目录，即：learning-python/packages 目录
# 而在这个目录下，并不存在 packages 这个包，运行会报错
# 解决办法是在 sys.path 中加入根目录路径
dir_home = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(dir_home, "../"))

from packages_main import PackagesMain


# 每个模块都有一个名字，通过 __name__ 属性，可以判断模块是被导入与独立运行
if __name__ == '__main__':
    print('run by itself')
    print(sys.path)

    c = PackagesMain('name1')
    c.say()
