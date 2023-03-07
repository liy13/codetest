# 函数和递归
'''
1、函数定义：具有特定功能，可进行重用的代码块。IPO结构
            def 函数名 (<参数1,2,3...>)： # 形参，其实，python中，有一点挺好的，就是，不用为变量提前声明类型。
                语句块
                return

2、参数设置：参数可有可没有，但是"()"这个符号必须有
        必选参数和可选参数：根据是否有默认值区分，注意的是，同一个函数中，必选参数必须在可选参数的前面
        有限参数和无限参数：是否有 *b形式。b是任意变量名。可以通过循环遍历的方式，对b中元素进行浏览
        参数传递方式的区别：位置（默认）与指定形参名

3、返回值：  零个或多个
   注意：多个返回值时，可以用一个变量（此为元组了）接受，或者用，相应数量的变量（与对应返回值类型一致）接受

4、局部变量和全局变量： 我认为是相对而言的。
   变量：  
        分为基本数据类型变量（浮点数、整数等），组合数据类型变量（列表、元组等）。
        值得注意的是，基本数据类型变量就是变量，而组合数据类型是通过指针实现的。
   注： 
        可以通过global保留字在函数中，使用修改全局变量
        若组合数据类型变量，在函数中未定义，该变量为指针形式，此时，局部变量等同于全局变量

5、lambda函数：返回函数名作为结果，通常用作充当某个函数的函数形参。
   形式：     <函数名> = lambda <参数>：<表达式>  这里又是表达式喔，跟if二分支紧凑形式有些一致。和普通函数还有不一样的地方就是，参数没
              有时，不需要加"()"。这样可以通过函数名调用函数了。

6、递归：函数中调用函数。
       链条：相邻元素之间的递归关系。n!=n(n-1)!
       基例：不需要递归的元素。当n=0时，n!=1。
   基本形式：函数+分支语句。递归需要调用本身，如何调用，根据函数名调用。递归中必须存在基例和链条，如何区分，根据分支语句区分。

7、

8、pyinstaller库:这是一个库，可以将我们的.py源文件，直接打包为可执行文件。


'''
# def test():
#     return 1,2,"b"
# a=test()
# print(type(a)) #一个变量就是元组


# import time as t
# import turtle as tr

# def drawline(bug):#判断是否应该绘制这条线
#     tr.pendown() if bug else tr.penup() # pendown()和penup()函数不需要一一对应
#     tr.fd(40)
#     tr.right(90)

# # 汉诺塔问题。
# count = 1  
# def hanota(n,src,dst,mid):# 数量，起始柱、目标柱、中间柱
#     global count # 定义一个全局变量
#     if n==1:
#       #   print("{}：{}->{}".format(count,src,dst))
#         count+=1
#     else:
#         hanota(n-1,src,mid,dst)
#       #   print("{}：{}->{}".format(count,src,dst))
#         count+=1
#         hanota(n-1,mid,dst,src)

# hanota(8,'a','c','d')
# print("最终移动了多少步：{}".format(count))
    
# # # 科赫雪花
# from turtle import *
# def koth(size,n): # 长度，阶数
#     if n==0:
#         fd(size)
#     else:
#         for angle in [0,-60,120,-60]:
#             right(angle)
#             koth(size/3,n-1)

# def main():
#     setup(1200,1200,100,100)
#     penup()
#     goto(200,200)
#     pendown()
#     pensize(2)
#     pencolor("purple")
#     for i in range(3):
#         right(120) 
#         koth(400,3)
#     hideturtle()
#     done()
# main()
      




