# -*- coding:utf-8  -*-

#一个函数在内部调用自身本身，这个函数就是递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print fact(1)
print fact(5)
print fact(100)
print fact(500)
#print fact(1000)     #RuntimeError: maximum recursion depth exceeded

    #
    #使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
    #
    #解决递归调用栈溢出的方法是通过尾递归优化.尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

    #
    #虽然尾递归优化很好, 但python 不支持尾递归，递归深度超过1000时会报错
    #






