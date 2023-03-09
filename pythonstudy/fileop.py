# 文件的使用
'''
1、文件的类型
   文件：数据的抽象和集合。文件都是以二进制形式存储在计算机中的。
   文本文件和二进制文件：根据文件内数据是否有统一编码，可以有不同的展示形式。
                       若数据编码格式统一，则可以展示为文本文件，可以看作一个存储着的长字符串。如.txt、.py等
                       否则只能展示为二进制文件。如.png、.avi等


2、文件的打开和关闭
   处理步骤：打开--操作--关闭
   open(<文件名>[,<打开模式>]):打开函数，格式为：<变量名> = open (<文件名> , <打开模式>)
   变量名：  文件句柄
   文件名：  绝对路径或者相对路径。注意，文件的存储路径中，由于"\"表示为转义符，所以最好使用"/"或"\\"进行替换
   打开模式：文本or二进制？读or写？
            r  只读，默认值，文件不存在返回FileNotFoundError错误
            w  覆盖写，文件不存在则创建，存在则完全覆盖写
            x  创建写，文件不存在则创建，存在则返回FileExistError
            a  追加写，文件不存在则创建，存在则在文件最后添加内容

            b  二进制文件模式
            t  文本文件模式，默认值
            +  与r/w/x/a一同使用，在原有功能基础上添加读/写功能。

    文件句柄.close():关闭函数

   
3、文件内容的读取
   方法：为什么不直接全部读取呢？如果一个文件十几个GB大小，那么会占用大量内存。
        <f>.read(size=-1)       读入前size长度内容,默认值为-1，即全部
        <f>.readline(size=-1)   读入一行前size长度内容，并自动跳到下一行。默认值为-1，即一行全部。
                                从文件操作指针当前位置，到结尾的行。如果是在一行末尾，那么不会输出。
        <f>.readlines(size=-1)  读入文件前size行，以每行为元素，返回一个列表。默认值为-1，即所有行
   注：逐行遍历有一个特殊的方法。for temp in fo,这样也可以达到逐行遍历的效果，且不需要read之类函数
    
4、数据的文件写入
   方法：
        <f>.write(str)          向文件中，写入一个字符串或字节流
        <f>.writelines(lines)   将一个元素全为字符串的列表，写入文件。其中元素直接拼接为一个整体字符串写入。
        <f>.seek(offset)        改变文件操作指针的位置。简单有三个，0-文件开头、1-当前位置、2-文件结尾。

注：map(funname,seq) 其中seq是可遍历的一组数据，对其中每个数据执行funname操作。返回的是一个map数据类型，所以需要类型转换。
'''

# # filepath1=input("请输入文本文件名：")
# filepath="pythonstudy/"+"threekingdoms.txt"
# fo = open(filepath,"rt",encoding="utf-8")
# for i in range(2):   # readline()可以自动换行。
#     print(fo.readline())
#     # tx=fo.readline()
# for i in fo:#这个会遍历所有。用的地方应该不多。
#     print(i)

#seek(offset), 这个函数很重要，所以，可能要自己去补充一下

# list1=["1","2","3"]   # map()返回的是一个map类的对象
# print(type(map(eval,list1)))

# # AutoTraceDraw.py 数据驱动程序
# import turtle as t
# t.title("自动轨迹绘制") # 海龟绘图窗口的标题
# t.setup(800,600)
# t.pencolor("red")
# t.pensize(5)
 
# #数据读取
# datals = []
# f = open("pythonstudy/autoturtle.txt","rt",encoding="utf-8")
# for i in f.readlines():
#     if i!="":
#         line = i.replace("\n","")
#       #   print(i)
#         datals.append(list(map(eval,line.split(","))))
# f.close()

# #自动绘制
# for i in range(len(datals)):
#     t.pencolor(datals[i][3],datals[i][4],datals[i][5])
#     t.fd(datals[i][0])
#     t.right(datals[i][2]) if datals[i][1] else t.left(datals[i][2])
# t.done()



