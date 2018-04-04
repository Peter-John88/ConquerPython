# -*-  coding:utf-8  -*-

    #
    #map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
    #
def f(x):
    return x*x
print map(f,[1,2,3,4,5,6,7,8,9])   #计算每个元素的平方

print map(str, [1,2,3,4,5,6,7,8,9])



    #
    #reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
    #reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    #
def add(x,y):
    return  x+y
print reduce(add,[1,3,5,7,9])   #对一个序列求和

def fn(x,y):
    return x*10+y
print reduce(fn,[1,3,5,7,9])

def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
print reduce(fn,map(char2num,'13579'))      #考虑到字符串str也是一个序列，配合map()，我们就可以写出把str转换为int的函数

def str2int(s):     #合并成一个函数
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))
print str2int('13579')


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y, map(char2num,s))
print str2int('13579')



    #
    #Excersise-1:利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
    #
def capitalize(s):
    return s.capitalize()
print map(capitalize, ['adam', 'LISA', 'barT'])

    #
    #Excersise-2:Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
    #
def prod(x,y):
    return x*y
print reduce(prod,[1,2,5,8])

def prod(L):
    return  reduce(lambda x,y:x*y, L)
print prod([1,2,5,8])







