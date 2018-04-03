#   -*- coding:utf-8  -*-

L=[x*x for x in range(10)]   #list comprehension
print L

g=(x*x for x in range(10))  #创建generator
print g

g=(x*x for x in range(10))
#print g.next()      #generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
for n in g:
    print n
#print [n for n in g]      #g是一个generator，列表推导式对此无用





def fib(max):   #斐波那契生成函数
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
print fib(6)
    # 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。




def fib(max):   #斐波那契生成函数
    n,a,b=0,0,1
    while n<max:
        yield b   #改成generator方式生成
        a,b=b,a+b
        n=n+1
    #
    #generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
    #
print fib(6)
for n in fib(6):
    print n




def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5
o=odd()
print o.next()
print o.next()
print o.next()
print o.next()
    #可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。


    #
    #在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
    #



