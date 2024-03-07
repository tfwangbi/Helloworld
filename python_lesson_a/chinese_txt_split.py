import jieba.posseg as posseg
import pandas as pd
import re

txt = "./../appdx/chinese_txt.txt"
# txt = "./../appdx/ldj.txt"
words = []

with open(txt, "r", encoding="utf-8") as fin:
    content = fin.read()

for word, flag in posseg.cut(content):

    if flag == "nr":
        words.append(word)

# print(words)

print(pd.Series(words).value_counts()[:20])


