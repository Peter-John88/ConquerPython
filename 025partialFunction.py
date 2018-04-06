# -*- coding:utf-8  -*-

print int('123')
print int('12345',base=8)
print int('12345',16)


def int2(x,base=2):
    return int(x,base)
print int2('10000')


    #
    #functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
    #
import  functools
int2 = functools.partial(int,base=2)
print int2('10000')
print int2('12345',base=10)   #base=2是默认参数，改成10也是ok的

    #简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
    #
    #创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数。

    #当传入：int2 = functools.partial(int, base=2)，实际上固定了int()函数的关键字参数base，也就是：int2('10010')。相当于：
    #kw = { base: 2 }
    #int('10010', **kw)
    #
    #当max2 = functools.partial(max, 10)，也就是：
    # args = (10, 5, 6, 7)
    #max(*args)


