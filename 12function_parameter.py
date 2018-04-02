# -*- coding:utf-8 -*-

###位置参数

def power(x):   #x^2
    return x*x
print power(5)
print power(15)


def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5,2)
print power(5,3)

#power(5)    #TypeError: power() missing 1 required positional argument: 'n'




###默认参数

def power(x,n=2):     #必选参数在前，默认参数在后，否则Python的解释器会报错（
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print power(5)
print power(5,2)



def enroll(name,gender,age=6,city="Beijing"):
    print 'name', name
    print 'gender', gender
    print 'age', age
    print 'city', city
print enroll('Sarah','F')
print enroll('Bob','M',7)
print enroll('Adam','M',city='Tianjin')


def add_end(L=[]):    #[]不是不可变对象，作为默认参数不合适。默认参数要用不可变对象
    L.append('END')
    return L
print add_end([1,2,3])
print add_end(['X','Y','Z'])
print add_end()
print add_end()



def add_end(L=None):  #None是不可变对象，作为默认参数是合适的
    if L is None:
        L=[]
    L.append('END')
    return L
print add_end()
print add_end()




###可变参数

    #可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print calc([1,2,3])
print calc((1,3,5,7))


def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print calc(1,2)   #可变函数调用的简化写法
print calc()

nums=[1,2,3]
print calc(*nums)  #在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去.这种写法很有用




###关键字参数

    #关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
    #关键字参数可以起到扩展函数的功能。比如收集用户注册时填写的除了必填信息以外的其他信息。
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print person('Michael',30)    #可以只传入必选参数
print person('Bob',35,city='Beijing')
print person('Adam',45,gender='M',job='Engineer')

extra={'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, city=extra['city'], job=extra['job'])
print person('Jack',24,**extra)




###命名关键字参数--python3才支持

    #检查是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print 'name:', name, 'age:', age, 'other:', kw
print person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)    #但是调用者仍可以传入不受限制的关键字参数

    #只接收city和job作为关键字参数
#def person(name, age, * ,city,job):    #命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#    print(name,age,city,job)
#print(person('Jack',24,city='Beijing',job='Engineer'))



###参数组合

    #
    #参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
    #

def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args =',args,'kw =',kw
print func(1,2)
print func(1,2,c=3)
print func(1,2,3,'a','b')
print func(1,2,3,'a','b',x=99)

args=(1,2,3,4)
kw={'x':99}
print func(*args,**kw)   #通过一个tuple和dict，你也可以调用该函数

    #
    #使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    #


