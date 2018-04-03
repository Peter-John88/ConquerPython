# -*-  coding:utf-8  -*-

    #
    #任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
    #

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print key    #因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

for value in d.itervalues():
    print value

for k,v in d.iteritems():
    print k,v




for ch in 'ABC':
    print ch





from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)






for i,value in enumerate(['A','B','C']):  #Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
    print i,value

for x,y in [(1,1),(2,4),(3,9)]:
    print x,y

for z in [(1,1),(2,4),(3,9)]:
    print z


