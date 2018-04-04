# -*- coding:utf-8  -*-


####dict

d={'Michael':95, 'Bob':75, 'Tracy':85}
print d
print d['Michael']

d['Adam']=67
print d['Adam']

d['Jack']=90
print d['Jack']
d['Jack']=88
print d['Jack']
print d

#d['Thomas']   KeyError

print 'Thomas' in d

print d.get('Thomas')
print d.get('Thomas',-1)

print d
d.pop('Bob')
print d

    #
    #和list比较，dict有以下几个特点：查找和插入的速度极快，不会随着key的增加而增加；需要占用大量的内存，内存浪费多。
    #
    #dict的key必须是不可变对象。

#key=[1,2,3]
#d[key]='a list'    #TypeError: unhashable type: 'list'



####set

s=set([1,2,3])
print s

s=set([1,1,2,2,3,3])
print s

s.add(4)
print s

s.add(4)
print s

s.remove(4)
print s

s1=set([1,2,3])
s2=set([2,3,4])
print s1&s2
print s1|s2

    #
    #set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
    #

# s=set([1,2,[1,2,3],3])    #TypeError: unhashable type: 'list'




####unhashable object

a=['c','b','a']  #unhashable
a.sort()
print a

a='abc'   #hashable
b=a.replace('a','A')  #new object
print b
print a


t={(1, 2, 3):95, 'Adam':98}     #(1, 2, 3) is hashable, can work as key in dict
print t

t={(1, [2, 3]):95, 'Adam':98}    #TypeError: unhashable type: 'list'







