# -*- coding: utf-8 -*-
"""백준1316

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kKFkMYu9kx6n8jWZL9_ci7lMf2mApWR8
"""

# 그룹 단어 체커
N = int(input())
cnt = 0
for i in range(N):
    result = True
    word_list = []
    word = input()
    if len(word) == 1:
        cnt += 1
        continue
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            word_list.append(word[i])
    word_list.append(word[i+1])
    for j in word_list:
        if word_list.count(j) > 1:
            result = False
    if result == True:
        cnt += 1
print(cnt)