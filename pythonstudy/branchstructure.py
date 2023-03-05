'''
1、if分支结构：
   单分支： if   <条件>：
                语句块
   双分支： if   <条件>：
                  ...
           else:
                  ...
   双分支紧凑形式：<表达式1> if <条件> else <表达式2> 注意，表达式不是赋值语句。紧凑形式不支持赋值语句
   多分支： if   <条件1>：
                  ...
           elif <条件2>:
                  ...
           elif <条件3>：
                  ...
           ...
   注意各个条件的先后与包含关系
   
2、条件判断操作符：  <、<=、>、>=、==、!=
3、条件组合的保留字：and--与、or--或、not--非、False 与 True
4、异常处理： try:
                 语句块1
             except: 
                 语句块2（语句块1发生错误，可以对针对某些错误，设置多个except进行不同处理）
             else: 
                 语句块3（语句块1无异常执行，“奖励”执行）
             finally:
                 语句块4（无论语句块1是否异常，都会执行）                 
    注：
       except后面可以加异常类型名（所有异常类型名都是提取预定义的）
       except可以有多个
5、             
'''

#CalBMIv3.py
height,weight = eval(input("请输入身高（米）与体重（千克），数值用逗号隔开："))
bmi = weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who,nat = "",""
if bmi < 18.5:
    who,nat="偏廋","偏瘦"
elif bmi>=18.5 and bmi <=24:# 18.5 <= bmi <= 24这种方式是可行的
    who,nat="正常","正常"
elif bmi>24 and bmi<25:
    who,nat="正常","偏胖"
elif bmi>=25 and bmi<28:
    who,nat="偏胖","偏胖"
elif bmi>=28 and bmi<30:
    who,nat="偏胖","肥胖"
else:
    who,nat="肥胖","肥胖"
print("国际标准：{}国内标准：{}".format(who,nat))