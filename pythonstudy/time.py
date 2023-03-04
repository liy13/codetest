# time库的学习
# 1、获取系统时间，对时间进行格式化输出
# 2、提供精确计时，常用于程序性能分析
''' 
  1、获取时间：
             time.time()   返回系统内部时间戳（以秒为单位，从1970年1月1日0点...开始），很长的浮点数。
             time.ctime()  返回一个字符串，形式为："星期 月 日 时：分：秒 年"。
             time.gmtime() 返回一个可以字符串结构,用变量接收。time.struct_time(tm_year,tm_mon,tm_mday,tm_hou,tm_min,tm_sec,tm_
                           tm_wday,tm_yday...)不用记，因为没必要，到时候再去翻就行。只需要记得有这样一种格式就行
  2、时间格式化：怎样的格式来表示时间。
             strftime(tpl,str)    strftime("%Y %m %d %H %M %S",time.gmtime()),其中分别为年、月、日、时、分、秒。我们可以任意组合插入
                                  其中%Y，%m...之类称之为时间格式化字符串，有很多，包括星期等，记住常见的就行
             strptime(str,tpl)    就是将一个时间的字符串表示为时间的结构变量。反转，注意tpl的一一对应关系就行
  3、程序计时：
             perf_counter() 返回一个cpu级别的精确时间数值，单位为秒。由于计数时候的起点不确定，所以调用一次无意义，连续调用差值才具有意义。       
  4、其它函数：
             sleep(s)       让程序休眠，单位是秒，可以是浮点数

'''
# #文本进度条
# import time
# scale=10 #程序的规模
# print("------程序开始------",end="\n")
# for i in range(0,scale+1):
#     a=i*"*"
#     b="."*(scale-i)
#     c=(i/scale)
#     print("{:^5.0%}[{}->{}]".format(c,a,b),end="\r")
#     time.sleep(0.2)
# print("\n------程序结束------")

# import time #其实不推荐这样直接用time.time()，因为这样的时间戳是不如perf_counter()精确的
# scale=100 #程序规模
# print("程序开始".center(scale,"-"))
# start = time.time()
# for i in range(0,scale+1):
#     a="*"*i
#     b="."*(scale-i)
#     c=i/scale
#     dur=time.time()-start
#     print("\r{:^5.0%}[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
#     time.sleep(0.01)
# print("")
# print("程序结束".center(scale,"-"))



