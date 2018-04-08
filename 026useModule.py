# -*- coding:utf-8  -*-

    #举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
    #现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：

    #mycompany
    #├─ __init__.py
    #├─ abc.py
    #└─ xyz.py

    #引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
    #请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。



    #模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

    #创建自己的模块时，要注意：
    #模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
    #模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。


###定义一个模块

' a test module'         #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__='xiaoshu'     #作者

import sys
def test():
    args=sys.argv            #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称。
    if len(args)==1:
        print 'Hello, World!'
    elif len(args)==2:
        print 'Hello, %s' %args[1]
    else:
        print 'too many arguments!'

if __name__=='__main__':
    test()
    #
    #当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    #



###作用域

    #类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
    #之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

def _private1(name):
    return 'hello, %s' % name

def _private2(name):
    return 'hello, %s' % name

def greeting(name):
    if len(name)>3:
        return _private1(name)
    else:
        return _private2(name)
    #
    #我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
    #




