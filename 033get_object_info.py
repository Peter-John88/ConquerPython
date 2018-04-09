#   -*- coding:utf-8   -*-

    #当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

###使用type()

    #首先，我们来判断对象类型，使用type()函数.  基本类型都可以用type()判断：
print type(123)
print type('str')
print type(None)

    #如果一个变量指向函数或者类，也可以用type()判断：
print type(abs)

class Animal(object):
    pass
a = Animal()
print type(a)

    #但是type()函数返回的是什么类型呢？它返回type类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print type(123)==type(456)
print type('123')==type('abc')
print type('123')==type(123)

    #但是这种写法太麻烦，Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：
import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType

    #最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：
type(int)==type(str)==types.TypeType



###使用isinstance()

    #对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

    #我们回顾上次的例子，如果继承关系是：object -> Animal -> Dog -> Husky
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a=Animal()
d=Dog()
h=Husky()

print isinstance(h,Husky)
print isinstance(h,Dog)

    #h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，h也还是Dog类型。换句话说，isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print isinstance(h,Animal)    #h还是Animal类型
print isinstance(d,Dog) and isinstance(d,Animal)   #实际类型是Dog的d也是Animal类型
print isinstance(d,Husky)   #d不是Husky类型

    #能用type()判断的基本类型也可以用isinstance()判断：
print isinstance('a',str)
print isinstance(u'a',unicode)
print isinstance('a',unicode)

    #并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
print isinstance('a',(str,unicode))
print isinstance(u'a',(str,unicode))

    #由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
print isinstance(u'a',basestring)




### 使用dir()

    #如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir('ABC')

    #类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print len('ABC')
print 'ABC'.__len__()

    #我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyObject(object):
    def __len__(self):
        return 100
obj=MyObject()
print len(obj)

    #剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print 'ABC'.lower()

    #仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()
print hasattr(obj,'x')
print obj.x
print hasattr(obj,'y')
setattr(obj,'y',9)
print hasattr(obj,'y')
print getattr(obj,'y')
print obj.y

    #如果试图获取不存在的属性，会抛出AttributeError的错误：
    #AttributeError: 'MyObject' object has no attribute 'z'

    #可以传入一个default参数，如果属性不存在，就返回默认值：
print getattr(obj,'z',404)

    #也可以获得对象的方法：
print hasattr(obj,'power')
print getattr(obj,'power')
fn=getattr(obj,'power')
print fn
print fn()


### 小结

    #通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：sum = obj.x + obj.y

    #就不要写：sum = getattr(obj, 'x') + getattr(obj, 'y')

    #一个正确的用法的例子如下：
def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None
    #假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

    #请注意，在Python这类动态语言中，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。




