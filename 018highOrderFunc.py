# -*- coding:utf-8  -*-

#变量可以指向函数

print abs(-10)

f=abs
print f
print f(-10)



#函数名也是变量
#abs =10
#abs(-10)     #TypeError: 'int' object is not callable




#传入函数

def add(x,y,f):
    return f(x) + f(y)
print add(-5,6,abs)



    #
    #把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
    #

