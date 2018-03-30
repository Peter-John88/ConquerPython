# -*- coding:utf-8 -*-

print abs(-1)
# abs(1,2)   #TypeError: abs() takes exactly one argument (2 given)
# abs('a')   #TypeError: bad operand type for abs(): 'str'

print cmp(1,2)
print cmp(1,1)
print cmp(2,1)


### type convert

print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool(0)
print bool('')


a=abs
print a(-1)

