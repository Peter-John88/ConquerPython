

#创建一个平方数的列表
squares=[]
for x in range(10):
    squares.append(x**2)
squares

squares=[x**2 for x in range(10)]    #列表推导式

squares = map(lambda x: x**2, range(10))  #lambda表达式

# 找出两个list元素不相等的组合
[ (x,y)  for x in [1,2,3] for y in [3,1,4] if x!=y]    #返回tuple，注意加括号





vec = [-4,-2,0,2,4]
[x*2 for x in vec]
[x for x in vec if x>=0]
[abs(x) for x in vec]
freshfruit=['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip()  for weapon in freshfruit]
[(x,x**2) for x in range(6)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

from math import pi
[str(round(pi,i))   for i in range(1,6)]






#####2.Nested List Comprehensions#####

#用列表推导式实现矩阵的转置
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

[[ row[i] for row in matrix ] for i in range(4)]    #注意前面一个含有方括号，是列表推导式，嵌套


