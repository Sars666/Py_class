'''
本题要求:

（1）选择一部长度合适的小说，中文、英文或其他语种皆可，长度不低于5万字。√

（2）首先对文本进行词（字）频统计，中文可以进行分词统计词频，或不分词统计字频，英文要求统计词频并考虑词语的大小写等价性。√(如何统计字频)

（3）按照词频顺序列出所有的词及其出现次数；√

（4）绘制排序-数量曲线，验证Zipf-Law（可以用第三方软件绘图）。√

（5）利用正则表达式查找文件中的某种特定模式，对这种模式进行提取分析。要求提取出的内容有一定的复杂性（多种匹配结果），提取的数量不低于20个。

（6）完成说明文档，其中包括程序的说明和结果分析的说明。

（7）提交压缩文件，其中包括：源文件，处理的小说文本文件，处理得到的统计数据，项目文档。

'''

import jieba
import matplotlib.pyplot as plt
from math import log10
import regex as re

#读取文本文件
filename = 'SecretOfSkin.txt'
with open(filename, 'rt') as f:
    book = f.read()

#汉字列表characterList
characterList = []
for line in book:
    for character in line:
        if '\u4E00' <= character <= '\u9FA5':
            characterList.append(character)


#用字典记录词语及其出现次数
wordDic = {}
for word in characterList:
    wordDic[word] = wordDic.get(word, 0) + 1


#结果排序
result = [(v, k) for k, v in wordDic.items()]
result.sort(reverse= True)

#打印结果表
resultPrint=[]
for j in range (len(result)):
    a = '**' * (7-len(result[j][1])) +      '\t\t'
    b = '*' * (10-len(str(result[j][0]))) + '\t\t'
    print('word: ' + str(result[j][1]) + a
            +'count: ' + str(result[j][0]) + b
            + 'rank: ' + str(j+1))


#去除汉字外的字符,并写入横纵坐标列表
rank = []
count = []
for i in result:
    count.append(log10(i[0]))
for i in range(len(count)) :
    rank.append(log10(i+1))

#matplotlib画图
plt.plot(rank, count, marker='^', mec='b', mfc='w',label="curve_plot")
plt.xlabel("rank")
plt.xlim(-0.5,4.5)
plt.xticks(range(5),('0','10','100','1000','10000'))
plt.yticks(range(5),('0','10','100','1000','10000'))
plt.ylim(-0.5,4.5)
plt.ylabel("count")
plt.title("Zipf's law? ---- character frequency")
plt.show()
