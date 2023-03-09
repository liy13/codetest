# 程序设计思想
'''
1、自顶向下设计与自底向上执行。最常见的程序设计方法之一
   其中，自顶向下设计是将一个大问题分成各个小问题，再针对每个小问题，分为小小问题。可嵌套，与树结构类似
   自底向上执行。对“树”末端进行单元测试开发，然后再逐步进行组合测试开发，直到最后形成结果。
2、   
'''
import random as rd
# 体育竞技分析
def printinfo():
    print("这是对于一场比赛的模拟")

def getParter():
    a,b,c=eval(input("请输入两个人的能力值，和模拟比赛的场数，用，分割："))
    return a,b,c


def gameOver(an,bn):
    if an==15 or bn==15:
        return True
    return False

def gamesOne(a,b):
    bug=rd.random()
    wina,winb=0,0
    if bug>=0.5:
        seving = "A" 
    else:
        seving = "B"
    an,bn=0,0
    for i in range(5):
        while not gameOver(an,bn):
            bug2=rd.random()
            if 0<=bug2<=(a/(a+b)):
                an+=1
            else:
                bn+=1
        if an==15:
            wina+=1
        else:
            winb+=1
    # print("A获胜次数{}和B获胜次数{}".format(wina,winb))
    if wina>winb:
        return True
    return False

def gamesNum(a,b,c):
    anums,bnums=0,0
    for i in range(c):
        if gamesOne(a,b):
            anums += 1
        else:
            bnums += 1
    return anums,bnums

def main():
    printinfo()
    proba,probb,n=getParter()
    an,bn=gamesNum(proba,probb,n)
    print("在{}局中，A获胜次数为{}，获胜概率为{:.2%}".format(n,an,an/(bn+an)))
main()

# 现在的深度学习算法用的就是半数学半计算思维，如果可以直接用简单的计算思维替代复杂的数学思维，应该会是深度学习领域一项重大的突破

# 天气预报MM5模型，通过对全球海量天气数据的模拟，演化出对于未来天气的推演。
# 股市也是如此，如果可以考虑到全球所有的数据，进行模拟，那么是否就可以一定程度地预测未来？
# 计算思维关注的是，如何对计算过程进行抽象。关注设计和构造，而非因果。

# 计算生态：开源项目、开源思想。没有顶层设计、以功能为单位、具备三个特点：竞争发展、相互依存、迅速更迭
# 数据处理领域，有一个非常基础的库，Numpy。其在处理大数据的时候，可以达到跟C语言编程运行相当的速率。底层就是C语言编写的，而接口是python语言

# python很重要的思想，就是站在巨人的肩膀上，善于使用已有的第三方库。
# 编程只是手段，而不是目的，最终的目的是为人类服务，所以要善于优化用户体验。
# 如进度条、进度展示、学会异常处理（处理错误输入、文件错误读写时等）、打印输出（过程信息、日志、帮助信息等）
 
# 基本的程序设计模式
# IPO  模块化设计 松紧耦合 自顶向下、自底向上  数据驱动 配置化设计，将数据与程序分割开。使用配置数据驱动程序执行（关键在于文件接口）




