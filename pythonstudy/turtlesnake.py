# import turtle，海龟绘图体系中，最小的单位是像素。所以...一切单位以像素为主
# turtle绘图体系中，有两个坐标系，
# 空间（四个象限那个，绘图窗口中心为零点）、角度（逆时针为正方向，顺时针为反方向）。
# 有两个视图，
# 一个是绝对的视图（相对于坐标系而言，由于坐标系是给定的，所以无论海龟在那个位置，调用相应函数的意义都是一样的）
# goto(x,y),让海龟去到（x,y）坐标。set(h),使得海龟回到相应h的方向。
# 一个是海龟的视图
# fd(距离)+bk（距离），前进+后退。
# circle(r,tangle),r有正负，左正右负。海龟相对于自己的左右距离为r的圆心，移动相应角度
# right(),left()，相对于自己左右调整方向
# hideturtle() 隐藏海龟

'''操纵海龟的函数，penup/pendown简写为pu/pd,还有pensize/width这两个函数相同，之所以采用
   这种看似冗余的方式，是为了编写程序的方便。对了，单位还是像素。
   pencolor(颜色字符串-小写或者R,G,B的值--小数值或者元组值)也是'''
import turtle
'''turtle.setup(width,height,startx,starty),四个元素，定义绘图窗口长宽和位置（距离屏幕左上方的位置）
   这个函数不是必须的，函数后面两个参数也不是必须的（默认为电脑屏幕正中心）'''
turtle.setup(650,350,200,400)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done() # 使得程序不会自动退出


'''RGB每个通道的取值有整数（0-255）和小数（0-1）之分，255对应1。'''
'''turtle.colormode（1.0/255）,修改使用RGB的形式'''
'''import是引用库名，使用这个库的函数时，则需要用库名.函数名(参数)形式，那是否可以省去库名呢？
   1、这里需要使用from 库名 import 函数a,函数b/*（全部）的形式。
   2、import 库名 as 库别名的方式'''
'''for in range(n)  i从0-（n-1）
   range(n)   [0,n-1]
   range(m,n) [m,n-1]'''
