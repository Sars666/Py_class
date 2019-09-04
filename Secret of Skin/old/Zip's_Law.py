'''
本题要求:

（1）选择部长度合适的小说，中文、英文或其他语种皆可，长度不低于5万字。√

（2）首先对文本进行词（字）频统计，中文可以进行分词统计词频，或不分词统计字频，英文要求统计词频并考虑词语的大小写等价性。√

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
from collections import Counter

#读取文本文件
filename = 'SecretOfSkin.txt'
with open(filename, 'rt') as f:
    book = f.read()

#分出汉字characterList
characterList = []
for line in book:
    for character in line:
        if '\u4E00' <= character <= '\u9FA5':
            characterList.append(character)
#结巴库分词
seg_list = jieba.lcut(book)
wordList = "/ ".join(seg_list).split('/ ')

#词频统计wordDic
def get_wordDic(List):
    wordDic = {}
    wordBook = List
    for word in wordBook:
        wordDic[word] = wordDic.get(word, 0) + 1
    for k in wordDic.keys():
        if not '\u4E00' <= k <= '\u9FA5':
            wordDic[k] = 0
    return wordDic

#结果排序
def result_sort(wordDic):
    result = [(v, k) for k, v in wordDic.items()]
    result.sort(reverse= True)
    return result

#打印结果表
def print_result(result):
    resultPrint=[]
    print('\nResult:\n')
    for j in range (len(result)):
        if result[j][0]!= 0:
            a = '**' * (7-len(result[j][1])) +      '\t\t'
            b = '*' * (10-len(str(result[j][0]))) + '\t\t'
            print('word: ' + str(result[j][1]) + a
                  +'count: ' + str(result[j][0]) + b
                  + 'rank: ' + str(j+1))

#去除汉字外的字符,并写入横纵坐标列表
def get_rankAndcount(result):
    rank = []
    count = []
    for i in result:
        if i[0] != 0:
            count.append(log10(i[0]))
    for i in range(len(count)) :
        rank.append(log10(i+1))
    return (rank,count)


wordDic_1 = get_wordDic(wordList)
wordDic_2 = get_wordDic(characterList)
result_1 = result_sort(wordDic_1)
result_2 = result_sort(wordDic_2)

print_result(result_1)
print_result(result_2)

rank_1 = get_rankAndcount(result_1)[0]
count_1 = get_rankAndcount(result_1)[1]
rank_2 = get_rankAndcount(result_2)[0]
count_2 = get_rankAndcount(result_2)[1]

#matplotlib画图
plt.plot(rank_1, count_1, marker='o', mec='red', mfc='w',label="word Frequency")
plt.plot(rank_2, count_2, marker='+', mec='blue', mfc='w',label="character Frequency")
plt.xlabel("rank")
plt.xlim(-0.5,4.5)
plt.xticks(range(5),('0','10','100','1000','10000'))
plt.yticks(range(5),('0','10','100','1000','10000'))
plt.ylim(-0.5,4.5)
plt.ylabel("count")
plt.title("Zipf's law")
plt.grid(True)
plt.legend()
plt.show()

match_regex = '皮肤的(.*?)'
things = []
for i in re.finditer(match_regex, book):
    who = i.group(1)
    things.append(who)
c = Counter(things)
for k,v in c.most_common(10):
    print(k,v)