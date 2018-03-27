# Ref from : http://python.jobbole.com/88940/


### 1.变量 ###

one =1
two =2
some_number=10000

# booleanstrue_boolean = True
# false_boolean = False
# stringmy_name = "Leandro Tk"
# floatbook_price = 15.80


###2.控制流程：条件语句###

if True:
    print "Hello Python If"
    if 2 > 1:
        print "2 if greater than 1"


if 1>2:
    print "1 is greater than 2"
else:
    print "1 is not greater than 2"


if 1>2:
    print "1 is greater than 2"
elif 2>1:
    print "1 is not greater than 2"
else:
    print "1 is equal to 2"



###3. 循环和迭代###

num =1
while num <=10:
    print num
    num += 1

loop_condition=True
while loop_condition:
    print "Loop Condition keeps: %s" %(loop_condition)
    loop_condition=False

for i in range(1,11):
    print i


###4.List：集合 | 数组 | 数据结构###


my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4

relatives_names = [  "Toshiaki",  "Juliana",  "Yuji",  "Bruno",  "Kaio"]
print(relatives_names[4]) # Kaio

bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
bookshelf.append(0)
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work W
print bookshelf[2]



###5.字典：Key-Value 数据结构###

dictionary_example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
print dictionary_example

dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian"
}
print "My name is %s" %(dictionary_tk["name"])
print "But you can call me %s" %(dictionary_tk["nickname"])
print "And by the way I'm %s" %(dictionary_tk["nationality"])

dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian",
    "age":24
}
print "My name is %s" %(dictionary_tk["name"])
print "But you can call me %s" %(dictionary_tk["nickname"])
print "And by the way I'm %i and %s" %(dictionary_tk["age"], dictionary_tk["nationality"])


###6.迭代：通过数据结构进行循环###

bookshelf = [
    "The Effective Engineer",
    "The 4 hours work week",
    "Zero to One",
    "Lean Startup",
    "Hooked"
]
for book in bookshelf:
    print book

dictionary={"some_key":"some_value"}
for key in dictionary:
    print "%s --> %s" %(key, dictionary[key])

dictionary={"some_key":"some_value"}
for key,value in dictionary.items():
    print "%s --> %s" %(key,value)

dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian",
    "age": 24
}
for attribute, value in dictionary_tk.items():
    print "My %s is %s" %(attribute, value)

###7.类&对象###


class Vehicle:   #定义一个类
    pass
car=Vehicle()    #实例化
print car

class Vehicle:
    #用构造函数，定义一个类在初始化的时候接受的参数
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
tesla_model_s = Vehicle(4,'electric',5,250)   #创建一个对象

class Vehicle:
    #用构造函数，定义一个类在初始化的时候接受的参数
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    def number_of_wheels(self):  #获取属性值
        return self.number_of_wheels
    def set_number_of_wheels(self,number):  #给属性设置新的值
        self.number_of_wheels=number

class Vehicle:
    #用构造函数，定义一个类在初始化的时候接受的参数
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    #使用@property (修饰符)来定义getters和setters
    @property
    def number_of_wheels(self):  #获取属性值
        return self.number_of_wheels
    @number_of_wheels.setter
    def set_number_of_wheels(self,number):  #给属性设置新的值
        self.number_of_wheels=number
tesla_model_s=Vehicle(4,'electric',5,250)
print tesla_model_s.number_of_wheels    #将这些方法作为属性使用

class Vehicle:
    #用构造函数，定义一个类在初始化的时候接受的参数
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    def make_noise(self):    #定义一个新方法
        print "VRUUUUUUUUM"
tesla_model_s=Vehicle(4,'electric',5,250)
tesla_model_s.make_noise()

###8.封装: 隐藏信息  --  公共实例变量###

class Person:
    def __init__(self, first_name): # 将 first_name 值作为参数应用于公共实例变量
        self.first_name = first_name
tk=Person('TK')
print tk.first_name

class Person:
    first_name='TK'    #不需要将 first_name 作为参数，所有的实例对象都有一个用 TK 初始化的类属性。
tk=Person()
print tk.first_name

class Person:
    def __init__(self, first_name): # 将 first_name 值作为参数应用于公共实例变量
        self.first_name = first_name
tk=Person('TK')
tk.first_name='kaio'   #更新值
print tk.first_name

###9.封装: 隐藏信息  --  Non-public实例变量###

    ##
    #有一个多数Python代码都会遵守的惯例：使用下划线作为前缀的命名(例如 _spam)应该被认为是API的非公开部分（不管是函数、方法还是数据成员）
    ##
class Person:
    def __init__(self,first_name, email):
        self.first_name=first_name
        self._email=email   #定义非公共变量
tk=Person('TK','tk@mail.com')
print tk._email

    ##
    #我们可以访问并更新它。非公共变量仅仅是一个惯用法，并且应该被当做API的非公共部分。
    ##
class Person:
    def __init__(self,first_name,email):
        self.first_name = first_name
        self._email = email
    def update_email(self,new_email):
        self._email=new_email
    def email(self):
        return self._email
tk = Person('TK', 'tk@mail.com')
print tk.email()
tk._email='new_tk@mail.com'      # 使用这两个方法来更新及访问非公开变量
print tk.email()
tk.update_email('new_tk2@mail.com')
print tk.email()


###10.封装: 隐藏信息  --  公共方法###

class Person:
    def __init__(self,first_name,age):
        self.first_name=first_name
        self._age=age
    def show_age(self):
        return self._age
tk = Person('TK',25)
print(tk.show_age())

###11.封装: 隐藏信息  --  非公共方法###

class Person:
    def __init__(self,first_name,age):
        self.first_name=first_name
        self._age=age
    def _show_age(self):
        return self._age
tk=Person('TK',25)
print tk._show_age()  #我们可以访问和更新它。 非公共的方法只是一个惯例，应该被视为API的非公开部分。

class Person:
    def __init__(self,first_name,age):
        self.first_name =first_name
        self._age=age
    def show_age(self):
        return self._get_age()
    def _get_age(self):
        return self._age
tk=Person('TK',25)
print tk.show_age()

    ##
    #通过封装，我们可以确保对象的内部表示是对外部隐藏的。
    ##



###11.继承：行为和特征###

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels=number_of_wheels
        self.seating_capacity=seating_capacity
        self.maximum_velocity=maximum_velocity
my_car = Car(4,5,250)
print my_car.number_of_wheels
print my_car.seating_capacity
print my_car.maximum_velocity

class ElectricCar(Car):   #在Python中，我们将父类作为子的参数来进行继承。 ElectricCar 类可以继承我们的 Car 类。
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)
my_electric_car = ElectricCar(4, 5, 250)
print(my_electric_car.number_of_wheels) # => 4
print(my_electric_car.seating_capacity) # => 5
print(my_electric_car.maximum_velocity) # => 250



















