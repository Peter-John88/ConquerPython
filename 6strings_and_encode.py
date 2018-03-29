# -*- coding: utf-8  -*-



###转义与不转义

print 'I\'m ok.'
print 'I\'m learning\nPython.'
print '\\\n\\'
print r'\\\n\\'

print '''
line 1
line2
line3
'''

print r'''
line 1
\n
line2
line3
'''


###编码

    ##
    #UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
    #
    #在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
    #用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
    #浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：

print ord('A')   # 字母A用ASCII编码是十进制的65
print chr(65)    # ASCII编码是十进制的65,对应字母A

print u'中文'   #以Unicode表示的字符串用u'...'表示
# u'中'      #u'\u4e2d'


     #把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
u'中文'.encode('utf-8')   #'\xe4\xb8\xad\xe6\x96\x87'

print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

    #把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法：
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')   #u'\u4e2d\u6587'



###格式化

print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%d.' %('Michael',  1000000)

print '%2d-%02d' % (3,1)   #指定宽度和是否用0填充
print '%02d-%02d' % (3,1)
print '%2d-%2d' % (3,1)
print '%.2f' % 3.1415926   #指定小数位

print 'Age: %s. Gender: %s'   %(25, True)
print u'Hi, %s' % u'Michael'
print 'growth rate: %d %%' % 7



