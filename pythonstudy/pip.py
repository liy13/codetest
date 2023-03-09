# python 第三方库
'''
更大的Python世界--第三方库
Python有一个全球社区，pypi.org,在里面根据关键字搜索相应的第三方库。但是，里面的资源由于是自然增长的原因，质量参差不齐，所以，可能需要其它的途径帮助我们挑选。
三种安装方法：
1、pip：
      常用命令:
               pip install <第三方库名> 默认是最新版本，可以通过"=="指定版本。如pytorch==0.1.1之类。也可以结合 -i <国内库链接>方式一定程度解决速度慢的问题    
               pip install -U <第三方库名>  更新当前第三方库
               pip uninstall <第三方库名>   卸载指定的第三方库
               pip download  <第三方库名>   下载但不安装第三方库，得到一个文件。
               pip show <第三方库名>        列出该库的详细信息
               pip search <关键词>          根据关键词检索第三方库，库名或者介绍信息之类有该关键字则会检索到
               pip list                     列出当前系统已经安装的第三方库
2、集成安装：批量安装第三方库的方式，如anaconda，它已经安装好了常见的800多个库，只要我们用其解释器或者环境的解释器就好

3、文件安装方式：某些第三方库需要编译再安装，如果系统没有这样的编译环境就会失败，所以有了这个，直接下载电脑对应的编译好了的版本。
                UCI页面：http://www.lfd.uci.edu/~gohlke/pythonlibs/ 这里提供相应内容  步骤：搜索->下载对应版本文件->pip install <文件名> 欧克

注：Python官方文档现在有了中文版，https://docs.python.org/zh-cn/3/  不建议初学者硬啃，因为缺少实例且很多专业术语，更多的是作为一本字典
           
'''

'''
os库：提供通用的、基本的操作系统交互功能。标准库，有几百个函数
入门功能：路径操作、进程管理、环境参数几类功能
         路径操作：os.path子库，处理文件路径及信息
         进程管理：启动系统中其他程序
         环境参数：获得系统软硬件信息等环境参数

路径操作：操作和处理文件路径。os.path子库
常用 import os.path as op
常用函数：
         abspath(path)      返回path在当前系统中的绝对路径,即使这个路径不存在也会返回一个绝对路径。就是在这个路径基础上，
                            根据当前程序所在文件夹进行添加
         normpath(path)     将路径无论变为标准形式。如"D:\\f\\1.txt"
         relpath(path)      返回当前程序与文件path之间的相对路径(relative path)
         dirname(path)      返回path的目录
         basename(path)     返回path中最后的文件名称
         join(path,*path)   组合path与paths，返回一个路径的串。相当于"+"
         exists(path)       判断path对应文件或者目录是否存在
         isfile(path)       判断path是否为已存在的文件
         isdir(path)        判断path是否为已存在的目录
         getatime(path)     返回上一次path的访问时间。返回一个标准时间戳，以s为单位的浮点数  access
         getmtime(path)     返回path对应文件或目录最近一次的修改时间 modify
         getctime(path)     返回path对应文件或目录的创建时间。  create 可以使用ctime()将这个时间戳转化为易读的形式
         getsize(path)      返回path对应文件的大小，以字节为单位

进程管理：os.system(command) 返回0时，表示脚本的执行退出状态成功
         执行程序或者命令command
注:当执行的是程序时，可以通过空格的方式添加参数 如"1.exe 参数1 参数2..."

环境参数：os库
        os.chdir(path)  修改当前程序操作的路径。虚拟修改，如os.chdir("D:")，虚拟修改当前程序绝对路径为D盘下
        os.getcwd()     返回程序的当前路径
        os.getlogin()   获得当前系统登录用户名称
        os.cpu_count()  获得当前系统的CPU数量
        os.urandom(n)   获得n个字节长度的随机字符串，通常用于加解密运算。有些字节无法展示时，用16进制替代展示。
          

一个简单的应用：第三方库自动安装脚本，就是运用os.command()


'''
# import os.path as op
# # print(op.abspath("1.txt"))  # 测试返回文件的绝对路径运行方式
# import os 
# print(os.getcwd())
# # os.chdir("C:")
# # print(os.getcwd()) #测试是否为虚拟路径，发现确实是虚拟路径，不实际更改存储位置



# import os
# libs=["1sdfsaf"] #我们所需要的第三方库
# try:
#     for lib in libs:
#         os.system("pip install"+lib)
#     print("安装成功") # 没有出现错误，指令正常执行时。
# except:
#     print("安装失败") 