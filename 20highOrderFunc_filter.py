# -*- coding:utf-8 -*-

    #
    #filter()也接收一个函数和一个序列.filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
    #用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
    #
def is_odd(n):   #在一个list中，删掉偶数，只保留奇数
    return n%2==1
print filter(is_odd, [1,2,4,5,6,9,10,15])


def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])



    #
    #Excersise-1:请尝试用filter()删除1~100的素数。
    #
def is_not_prime(n):
    for i in range(2,n):
        if n % i ==0:
            return True
            break
    return False
print filter(is_not_prime, range(1,101))







