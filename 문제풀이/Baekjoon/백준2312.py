# -*- coding: utf-8 -*-
"""백준2312

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UVx5jCYtUX14f9VoeAA2iSNGh8kzMynO
"""

# 수 복원하기
T = int(input())
for i in range(T):
    number = int(input())
    for j in range(2, number+1):
        cnt = 0
        if number % j == 0:
            while number % j == 0:
                number = number // j
                cnt += 1
        if cnt > 0:
            print(j, cnt)