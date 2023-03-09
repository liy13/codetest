# 数据组织的维度
'''
一维数据：
        表示：用列表、集合等  
        存储：通过向各个元素间插入符号，如空格、","、或者其它的特殊字符之类。最好插入的分割字符在元素中不会出现
        join()--返回一个字符串与split()--返回一个列表。对列表、字符串等进行操作。
二维数据：基础方式，就是通过列表嵌套列表元素的方式增加维度。

CSV数据存储方式：Comma-Separeted Values  .csv文件
每一行表示一个一维数据，每个一维数据之间使用","分割开。
注：若数据包含","。那么具体情况，具体处理，可能是通过转义符，或者用引号包裹

第三方库：wordcloud 
wordcloud 优秀的词云展示第三方库
词云： 以词语为基本单位，以图形可视化的方式，更加直观和艺术的展示文本。
wordcloud 库使用对象的方式调用方法。

步骤：
     w=wordcloud.WordCloud() 创建一个词云对象  配置参数调整相应信息
                             参数：你确定要记顺序？还是指定参数名来修改参数吧。
                                   width/height--单位像素,默认值为400/200。设置输出的图片尺寸
                                   min_font_size,    输出字体的最小字号， 默认值为4号  
                                   max_font_size,    输出字体的最大字号，默认值为20号
                                   font_step,        输出字体字号的步间间隔？默认值为1   这个不是很懂
                                   font_path,        自定义字体文件的路径，默认值为none  "msyh.ttc" 这个是微软雅黑
                                   max_words，       输出单词数量的上限，默认为两百
                                   stop_words,       指定不显示的单词，  参数为一个列表，元素为单词字符串
                                   mask,             指定词云输出的形状，需要引用imread()函数。
                                                     如:from scipy.misc import imread;mk=imread("pic.png");w=wordcloud.WordCloud(mask=mk);
                                   background_color  指定词云输出的背景颜色，默认值为黑色。

     w.generate(txt)         向这个对象中加载我们的文本  这个库中会自动对文本进行透明处理。 
                             首先以空格分割单词（中文就需要用到jieba库） 
                             然后根据单词出现次数对单词文本大小进行调整
                             会过滤掉长度为1或者2的单词 （未测试） 测试过，不会。
     w.to_file(filename)     将词云输出为图像文件，.png或者.jpg格式。如w.to_file("outfile.png")

                                




'''
# # 从csv文件中读入数据
# fo = open(fname)
# ls = []
# for line in fo:
#     line = line.replace("\n","")
#     ls.append(line.split(","))
# fo.close()
 
# #向csv文件中写入数据
# ls = [[],[],[]]
# f = open(fname,'w')
# for item in ls:
#     f.write(','.join(ls)+"\n")
# f.close()

# # wordcloud简单应用
# import jieba
# import wordcloud
# txt="今天是植树节。\
# 小猴想去野外种树。它好不容易才从森林里找了一棵小苹果树苗。小猴别提有多高兴了。\
# 小猴开始挖坑了。它挖了很长时间，可还是不合适。因为它挖的坑不是太小了，就是太浅了。小猴很着急。\
# 这时候，小兔刚好从这里经过。小兔说：“我来帮你挖坑吧。”小兔三下五除二地就把坑给挖好了。小猴说：“现在让我来栽树苗吧。”\
# 很快，树苗就栽好了。\
# 小猴说：“还有一件事没有办到。”小兔说：“是什么事呀？”\
# 小猴说：“是浇水呀。”\
# 小猴和小兔开始找水了。它们好不容易才找到一条小河，但是，找不到盛水的东西，这可怎么办呢。突然，小猴和小兔听到大大的脚步声，它俩吓得撒腿就想跑。可是由于太紧张，跑了没多远，它俩都跑不动了。这时候，它俩用手遮住眼睛，爬在地上一动不动。\
# “你们两个小家伙这是在干嘛呢，跑什么呀？”小猴和小兔睁开眼睛一看，原来是大象伯伯在说话。它俩这才松了一口气。\
# 小猴说：“我俩在种树，可是没水，这不，刚刚才找到了小河的水。”\
# 大象伯伯说：“哪不是挺好吗？”\
# 小兔说：“可我们没有盛水的东西。”\
# 大象伯伯说：“没事，没事。你们带我去小河边吧。”小猴和小兔就带着大象伯伯到了小河的地方。大象伯伯伸出它的长鼻子，开始“咕咚咕咚”的吸水了。吸完水后，它们三个就来到了种小树苗的地方。\
# 大象伯伯给小树苗浇了水之后，它们三个就各回各家了。"
# w=wordcloud.WordCloud(width=1000,height=700,font_path="STXIHEI.TTF")
# # str=jieba.lcut(txt)
# # print(str)
# w.generate(" ".join(jieba.lcut(txt)))
# w.to_file("wc1_test.png")

# wordcloud对于文本文件的使用  
import jieba
import wordcloud
from scipy.misc import imread
mk = imread("triangel.png")  #修改形状为三角形
# fo=open("pythonstudy/resource/countryimprove.txt",encoding="utf-8")
fo=open("pythonstudy/resource/newtime.txt",encoding="utf-8")
ls=jieba.lcut(fo.read())
lt=ls.copy() # 列表是指针啊，亲。所以如果只是赋值的话，它们指向的是同一片空间
for i in lt:
    if len(i)==1:
        ls.remove(i)

for i in ls:
    if i=="的":
        print("这就不科学了")
txt=" ".join(ls)
fo.close()

w=wordcloud.WordCloud(width=1000,height=700,font_path="STXIHEI.TTF",background_color="white",mask=mk)
# str=jieba.lcut(txt)
# print(str)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pythonstudy/resource/img/3.png")

# # # remove() 和pop()函数一样，就是，函数删除当前位置后，后面的位置会顶上来，而这个函数已经不会再遍历当前位置了
# ls=["的","的","的","的","的","的","的","的","的","的","的","的","的","的","的","的"]
# print(len(ls))
# for i in range(len(ls)-2):
#     if len(ls[i])==1:
#         ls.pop(i)
# print(len(ls))