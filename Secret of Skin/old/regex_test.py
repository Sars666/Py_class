import regex as re
from collections import Counter

#读取文本文件
filename = 'SecretOfSkin.txt'
with open(filename, 'rt') as f:
    book = f.read()

match_regex = '皮肤([^“”，。、：\s/《》]{2,4})[“”，。、：\s/《》]'
things = []
for i in re.finditer(match_regex, book):
    who = i.group(1)
    things.append(who)
c = Counter(things)
for k,v in c.most_common(20):
    print(k,v)