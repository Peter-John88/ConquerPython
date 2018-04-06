# -*-  coding:utf-8  -*-

def now():
    print '2014-09-01'
f=now      #函数可以赋值给变量，然后通过变量调用函数
print f()


        #也可以把匿名函数作为返回值返回
print now.__name__
print f.__name__



    #
    #现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
    #


    #本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
    #观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
def log(func):
    def wrapper(*args,**kw):
        print 'call %s' %func.__name__
        return func(*args,**kw)
    return wrapper

    #借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print '2015-01-01'
print now()     #调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志.
                #把@log放到now()函数的定义处，相当于执行了语句：now = log(now)


    #
    #由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
    #
    #wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。


    #如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s():' %(text, func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

    #这个3层嵌套的decorator用法如下：
@log('excute')
def now():
    print '2018-09-09'

print now()

    #和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)

    #
    #我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
    #

print now.__name__  # 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'

    #
    #因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
    #不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
    #

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return  wrapper

@log
def now():
    print '2018-09-09'
print now()

print now.__name__

    #或者针对带参数的decorator：

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)       #记住在定义wrapper()的前面加上@functools.wraps(func)。
        def wrapper(*args,**kw):
            print '%s %s()' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print '2018-09-09'

print now()




    #Excersise-1:请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
    #Excersise-2:再思考一下能否写出一个@log的decorator，使它都能支持如下两种装饰器：
@log
def f():
    pass

@log('execute')
def f():
    pass



