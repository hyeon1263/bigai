# -*- coding: utf-8 -*-
"""백준2217

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PLq3UAu2Uh_hA-ezJX9fjRlWqTDWuCqm
"""

# 로프

N = int(input())
rope_list = []
for i in range(N):
    rope = int(input())
    rope_list.append(rope)
rope_list.sort()

max = rope_list[0] * N
for i in range(N):
    if max < rope_list[i] * (N-i):
    
print(max)