# -*-   coding:utf-8  -*-



####list

classmates=['Michael','Bob','Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
#print classmates[3]  #list index out of range
print classmates[-1]
print classmates[-2]
print classmates[-3]
#print classmates[-4]

classmates.append("Adam")
print classmates
classmates.insert(1,'Jack')  #添加到指定位置
print classmates

classmates.pop()
print classmates
classmates.pop(1)
print classmates

classmates[1]='Sarah'
print classmates


L=['Apple',123,True]
print L
s=['python','java',['asp','php'],'scheme']
print len(s)

p=['asp','php']
s=['python','java',p,'scheme']
print s
print s[2][1]

L=[]
print len(L)




####tuple

classmates=('Michael','Bob','Tracy')
print classmates
print classmates[2]
print classmates[-1]

t=()
print t
t=(1,)  #not t=(1)
print t


t=('a','b',['A','B'])
print t
t[2][0]='X'
t[2][1]='Y'
print t














