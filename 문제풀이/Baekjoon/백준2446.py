# -*- coding: utf-8 -*-
"""백준2446

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HcEiuqh1mr3Mc6sqDYERxiHaLyos7fmb
"""

# 별 찍기 - 9

N = int(input())
for i in range(N,0,-1):
    print(' '*(N-i), end='')
    print('*'*(2*i-1))
for i in range(2,N+1):
    print(' '*(N-i), end='')
    print('*'*(2*i-1))