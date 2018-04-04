# -*-  coding:utf-8  -*-

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print my_abs(-1)



###空函数

def nop():
    pass     #pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

age=18
if age>=18:
    pass


###参数检查

#my_abs(1,2)     #TypeError: my_abs() takes exactly 1 argument (2 given)
print my_abs('A')     # 'A' ,不完善，没有做类型检查
#abs('A')        #TypeError: bad operand type for abs(): 'str'

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
#my_abs('A')    #TypeError: bad operand type




###返回多个值

import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print x,y
r=move(100,100,60,math.pi/6)
print r    #可以返回多值，返回的就是一个tuple







