# -*- coding: utf-8 -*-
"""백준1157

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15KD1yaIK51dtmuHvzOrMI1STPiPtmG-q
"""

# 단어 공부
word_d = {}
word = input()
word = word.upper()
for i in word:
    if i in word_d:
        word_d[i] += 1
    else:
        word_d[i] = 1
cnt = 1
max = 0
for k, v in word_d.items():
    if max < v:
        max = v
        cnt = 1
        max_key = k
    elif max == v:
        cnt += 1

if cnt == 1:
    print(max_key)
else:
    print('?')