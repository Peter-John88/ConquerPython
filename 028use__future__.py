# -*-  coding:utf-8  -*-

    #
    #由于Python是由社区推动的开源并且免费的开发语言，不受商业公司控制，因此，Python的改进往往比较激进，不兼容的情况时有发生。
    # Python为了确保你能顺利过渡到新版本，特别提供了__future__模块，让你在旧的版本中试验新版本的一些特性。
    #

#使用python3中字符串表示方法

from __future__ import division
from __future__ import unicode_literals
print '\'xxx\' is unicode?', isinstance('xxx', unicode)    #在3.x中，所有字符串都被视为unicode
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)   #在3.x中，所有字符串都被视为unicode
print '\'xxx\' is str?', isinstance('xxx',str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)  #在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。

#使用python3中的除法

print '10/3=',   10/3
print  '10.0/3=', 10.0/3
print  '10//3=',  10//3





