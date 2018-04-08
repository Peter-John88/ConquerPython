# -*-  coding:utf-8  -*-

# step1:安装pip
 #如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
 #如果你正在使用Windows，在安装Python时，确保安装时勾选了pip和Add python.exe to Path。
 #在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。

# ste2:安装和使用一个模块
 # 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索：
 # pip install pillow
from PIL import Image
im=Image.open('test.png')
print im.format, im.size, im.mode
im.thumbnail((200,200))
im.save('thumb.jpg','JPEG')
  #以上代码实现了图片的压缩

###模块搜索路径

  #默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
import sys
print sys.path

  #如果我们要添加自己的搜索目录，有两种方法：
  #一是直接修改sys.path，添加要搜索的目录，这种方法是在运行时修改，运行结束后失效。
import sys
sys.path.append('users/bailingguobl/pythoncode')
  #第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。























