# -*-  coding:utf-8  -*-

print range(1,11)

    #生成squares序列
L=[]
for x in range(1,11):
    L.append(x*x)
print L

print [x*x for x in range(1,11)]


print [x*x for x in range(1,11) if x%2==0]   #仅偶数的平方

print [m+n for m in 'ABC' for n in 'XYZ']    #使用两层循环，可以生成全排列


import os
print os.getcwd()
print [d for d in os.listdir('.')]    #列出当前目录下的所有文件和目录名



d={'x':'A', 'y':'B', 'z':'C'}
print [ k + '=' + v for k,v in d.iteritems()]  #遍历dict的key和value


L=['Hello','World','IBM','Apple']    #把一个list中所有的字符串变成小写：
print [s.lower() for s in L]


L=['Hello','World',18,'Apple',None]
#print [s.lower() for s in L]    #AttributeError: 'int' object has no attribute 'lower'

print isinstance('abc',str)
print isinstance(123,str)





