
lambda a,b:a+b      #a,b作为参数，返回a+b作为结果



#lambda表达式返回一个函数

def make_incrementor(n):
    return lambda x:x+n
f=make_incrementor(42) #<function <lambda> at 0x10d14d848>  lambda expressions return a function. f is a func.
f(0)  #42
f(1)  #41




#用lambda表达式返回一个函数作为参数

pairs = [(1, 'one'), (2, 'two'), (4, 'four'),(3, 'three') ]
pairs
pairs.sort()
pairs

pairs = [(1, 'one'), (2, 'two'), (4, 'four'),(3, 'three') ]
pairs
pairs.sort(key=lambda pair:pair[1])
pairs

pairs = [(1, 'one'), (2, 'two'), (4, 'four'),(3, 'three') ]
pairs
pairs.sort(key=lambda pair:pair[0])   # equal to : pairs.sort()
pairs



#结合map函数使用

squares = map(lambda x: x**2, range(10))
squares    #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

