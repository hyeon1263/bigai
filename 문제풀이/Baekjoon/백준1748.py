# -*- coding: utf-8 -*-
"""백준1748

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mw-Z9R4Wn_DzPMFIR1z-l0_5fI29kLw0
"""

# 수 이어 쓰기 1
N = input()
sum = 0
for i in range(1,len(N)):
    sum += i * (10**i - 10**(i-1))

sum += len(N) * (int(N) - 10**(len(N)-1) + 1)
print(sum)