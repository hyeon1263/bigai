# -*- coding: utf-8 -*-
"""백준2475

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hYqpGefK9-VDWtleBZ--1K6nNCbwN0Fh
"""

# 검증 수
a, b, c, d, e = map(int, input().split())

ans = (a**2 + b**2 + c**2 + d**2 + e**2) % 10
print(ans)