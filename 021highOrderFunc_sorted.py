# -*- coding:utf-8 -*-

print sorted([36, 5, 12, 9, 21])   #默认按升序排

def reversed_cmp(x,y):   #自定义倒序排列比较函数
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)   #倒序排


print sorted(['bob', 'about', 'Zoo', 'Credit'])



   #忽略大小写，按照字母序排序
def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return  -1
    if u1>u2:
        return 1
    return 0
print sorted( ['bob', 'about', 'Zoo', 'Credit'] ,cmp_ignore_case)



