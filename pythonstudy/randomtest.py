# python中随机库 random
'''
基本函数：
        seed(a=None):初始化随机种子，默认为调用时系统当前时间。
                     随机种子唯一确定一组随机序列，这样可以方便我们对随机过程进行复刻。
        random():生成一个[0.0,1.0)之间的随机小数，即顺序遍历由随机种子确定的随机序列。

扩展函数：
        randint(a,b):       返回[a,b]之间的一个随机整数
        randrange(a,b[,c]): 返回一个[a,b)之间，c为步长的随机整数
        getrandbits(k):     返回一个k比特长的随机整数
        uniform(a,b):       返回[a,b]之间的一个随机小数
        
        choice(seq):        从序列seq随机选择一个元素，seq可以为列表等
        shuffle(seq):       将序列seq随机打乱后，返回seq(seq已更改)
小技巧：
      多行代码合并为一行，  每行代码用";"分开
      一行代码分为连续多行，每行末尾添加"\"

'''

#CalPiV2.py
import time as t
from random import random #这里我犯了个错误，就是创建的文件名最好不要与要用到的库相同，不然，引用的是自己创建的文件。
dots=1000*1000*10 #点总数
start=t.perf_counter()
rsize=0 
for i in range(dots):
    # x,y=random.random(),random.random()
    x,y=random(),random()
    r=x**2+y**2
    if r<=1.0:
       rsize+=1
pi=4*rsize/dots
print("pi的值为{:.7f}".format(pi))
print("花费时间为：{:.5f}s".format(t.perf_counter()-start))

