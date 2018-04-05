# -*-  coding:utf-8   -*-

# ## 函数作为返回值

def calc_sum(*args):   # 定义一个可变参数的求和函数
    ax = 0
    for n in args:
        ax = ax+ n
    return ax
print calc_sum(1,2,3,4,5)


def lazy_sum(*args):   #可以不返回求和的结果，而是返回求和的函数！
    def calc_sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return calc_sum
f=lazy_sum(1,2,3,4,5)
print f
print f()


f1=lazy_sum(1,2,3,4,5)
f2=lazy_sum(1,2,3,4,5)
print f1==f2    #false   f1()和f2()的调用结果互不影响。



# ## 闭包


def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print f1(),f2(),f3()    #全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

    #返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

    #如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    fs=[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print f1(),f2(),f3()









