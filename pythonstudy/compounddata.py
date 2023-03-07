# 组合数据类型
'''
集合：与数学中集合概念一致。无序，且元素唯一。可以提供一组有重复的数据，得到一组无重复的数据。
1、创建：  set()和{}，元素之间用","分割开
2、操作符：
          S|T 并 ; S-T 差 ; S&T 交 ; S^T 补 ; 集合间运算，具有增强赋值操作符形式，如|=、-=、&=、^=。
          S<=T S<T S>=T S>T 表示包含关系，返回True/False。
3、操作方法：
          s.add(x)     如果x不在集合s中，则添加
          s.discard(x) 删除x，如集合s本身没有x，也不报错
          s.remove(x)  删除x，如集合s本身没有x，报KeyError异常（try-except方式处理）
          s.clear()    清空元素
          s.pop()      随机返回一个元素并将这个元素从s中删除，若s为空，报KeyError异常
          s.copy()       返回s的一个副本
          len(s)       返回s的元素个数
          x in s       s中是否有x
          x not in s   s中是否没有x
          set(x)       将其它类型变量转化为集合类型
4、应用场景： 数据去重、数据包含
注：
   因为元素唯一，所以其元素不可变。不可变数据类型有，如数字（整数、浮点数、复数）、字符串、元组等
   创建空集合时，只能使用set()，为什么？
   遍历一个循环时，集合内部元素的取出序列，是不可知的，与定义时后的集合元素排序不一定相同。但是不知道，第二次整体遍历和第一次整体遍历是不是一样的。

序列：基类，一组有序的元素。字符串、元组、列表从其衍生。所以，其很多方法值得了解。
1、序号：有正序和反序。
2、操作符：通用 
            x in/not in s      x是否是s的元素
            s+t                连接两个序列s和t
            s*n或n*s           序列s复制n次
            s[i]               索引,不改变s
            s[i:j[:k]]         切片,不改变s [i,j)
3、操作方法：通用
            len(s)             返回序列s长度
            min(s)/max(s)      返回序列s的最小/大元素，s中元素需要可比较（相同类型？）
            s.index(x[,i,j])   返回序列s[从i到j位置，]第一次出现元素x的位置
            s.count(x)         返回序列s中出现x的总次数


元组：一旦创建便不能进行修改的序列，继承了序列的所有通用操作符与方法。可以将函数的接口设置为元组形式，这样可以一定程度地保护数据
创建："()"与tuple(),也可以不用"()"直接通过s=a,b,c,d的形式设置一个元组，如return a,b,c,d 返回的就是一个元组。

列表：对于序列的扩展，元素可以修改。继承了序列的所有通用操作符与方法。
创建："[]"与list()。注意的是，这里创建了一片空间，返回指向这片空间的指针
操作方法：
        ls[i]        可以通过索引的方式对相应元素修改，如ls[i]=x 赋值;del ls[i] 删除;
        ls[i:j[:k]]  同样可以赋值和修改
        ls+=lt       将lt加到ls尾
        ls*=n        重复多少次
        sorted(ls)   对列表ls排序

        ls.append(x)    在列表ls后，添元素x
        ls.clear()      清空
        ls.copy()       返回副本，一个新的列表
        ls.insert(i,x)  i位置增加元素x,原先i位置及之后元素，向后挪
        ls.pop(i)       将i位置元素取出并删除
        ls.remove(x)    将列表ls中出现的第一个元素x删除(若有，只删除一个，没有就ValueError: list.remove(x): x not in list)
        ls.reverse()    翻转ls

        
字典：是映射的体现。一组无序的键值对，嗯，这里由点问题，因为不知道，循环遍历其值时，与我们定义时，顺序是否一致
键值对：键是对数据索引的扩展。比如说str中我们采用i数字的方式，而在键值对中，我们可以自定义，任何非可变数据类型
创建：{}与dict()。如{<键1><值1>,<键2><值2>,...}
处理函数及方法：
              del d[k]            删除字典d中对应键k的键值对
              k in d              键k是否在字典d中
              d.keys()            返回字典d中所有的键信息，返回的不是列表类型，可以遍历，字典的特殊类型
              d.values()          返回字典d中所有的值信息，返回的不是列表类型，可以遍历，字典的特殊类型
              d.items()           返回字典d中所有键值对信息
              d.get(k,<default>)  若键k存在，则返回对应值，否则返回default
              d.pop(k,<default>)  若键k存在，则取出对应值，否则返回default
              d.popitem()         随机从字典d中返回一个键值对，以元组形式返回。如(键，值)
              d.clear()           清空
              len(d)              返回字典d中键值对数目
应用场景：对映射的充分表达。因为我们可以自定义键,而键所对应的值，是任意的。
注："{}"可以创建一个空的字典，而不是一个空的集合。因为字典比集合更常用

第三方库：jieba
jieba:优秀的中文分词第三方库。将一段中文文本，通过分词，获得单个词语。
原理：利用一个中文词库，确定汉字之间的关联概率。关联概率大的，形成相应分词。而除了分词，用户还可以添加自定义的词组，以适应不同场景
三种模式：
        精确模式：   将文本严格切分开，不存在冗余，切分得到的词语组合起来即是原文
        全模式：     将文本中所有可能的词语都扫描出来，可能存在冗余，切分得到的词语组合起来不一定是原文
        搜索引擎模式：在精确模式的基础上，对长词再次切分。适合搜索引擎对于短词语的利用
函数：  
        jieba.lcut(s):              精确模式，切分的词语以列表返回
        jieba.lcut(s,cut_all=True): 全模式，返回还是一个列表
        jieba.lcut_for_search(s):   搜索引擎模式，返回一个列表，还是存在冗余。嗯，它保留了精确模式的分词结果，并在这个基础上
                                    对长词再次划分，划分出来的词语，添加到返回结果中 
        jieba.addword(w):           向词典添加新词     



'''

# s="123456"
# s[::-1] #切片不影响本身
# print(s) 
# tp=1,2,3,4,5,6  #看看元组是不是也是指针，不过，元组一旦创建不能够修改，所以，也没什么意义
# tc=tp

# ls=[1,2]
# ls*2   # 重复n次，也不修改本身
# print(ls)

# ls=[1,2,3,4] #测试remove函数是不只删除一个元素
# ls.remove(1)
# print(ls)

# d={1:2,2:[1,2,3]}  # 删除该键时，相应的键值对都会删除
# # del d[1]
# # print((1 in d))
# # print(type(d.values())) #真是特殊类型啊
# # print(d.popitem())  # 看随机返回的键值对，这个元组形式，是什么形式
# # print(d[2][0])
# print(d.items())

## 获得一组数据的统计信息
# def getNum():
#     ls=[]
#     temp=input("请输入一个数字，回车结束：")
#     while temp!="":
#         ls.append(eval(temp))
#         temp=input("请输入一个数字，回车结束：")
#     return ls

# def getMean(ls):
#     sum=0
#     for i in ls:
#        sum+=i
#     return sum/len(ls)

# def getDev(ls,mean):
#     dev=0.0
#     for i in ls:
#         dev += pow(i-mean,2)
#     return dev/(len(ls)-1)

# def getMediaNum(ls):
#     sorted(ls)
#     if len(ls)%2==0:
#         return (ls[len(ls)//2-1]+ls[len(ls)//2])/2
#     else:
#         return ls[len(ls)//2]
# ls=getNum()
# mean=getMean(ls)
# dev=getDev(ls,mean)
# mnum=getMediaNum(ls)
# print("平均值：{:.2f}方差：{:.2f}中间数：{:.2f}".format(mean,dev,mnum))

# # CalHamletV1.py
# def getText():
#     txt = open("pythonstudy/hamlet.txt","r").read()
#     txt = txt.lower()
#     for ch in '\'!#$%&()*+,-./:;<=>?@[\\]^_’{|}~':
#         txt = txt.replace(ch," ")
#     return txt

# hamlettxt = getText()
# words = hamlettxt.split()
# counts = {}
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# item = list(counts.items())
# item.sort(key=lambda x:x[1],reverse=True)  #这里是存在问题的，可以详细了解一下列表的排序方法
# for i in range(10):
#     word,count = item[i]
#     print("单词：{:^10} 次数：{:>5}".format(word,count))

## 三国演义的词频统计
import jieba
txt = open("pythonstudy/threekingdoms.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
excludes = {"将军","荆州","却说","二人","不可","不能","如此"} # 因为我们要做的是，人名的词频统计。所以，需要排除掉这些东西。这个方法
# 有点笨，应该有一个更智能的方法
counts = {}
for word in words:
    if len(word)==1 or (word in excludes):
        continue
    elif word == "诸葛亮" or word == "孔明曰" or word == "孔明": # 不断优化优化...好笨的方法，我就不继续了
        rword="诸葛亮"
    else:
        rword=word
    counts[rword] = counts.get(rword,0) + 1
items = list(counts.items())
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)  #这里是存在问题的，可以详细了解一下列表的排序方法
for i in range(15):
    word,count = items[i]
    print("单词：{:<10} 次数：{:>5}".format(word,count))