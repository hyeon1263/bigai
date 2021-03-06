# -*- coding: utf-8 -*-
"""백준1929

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MDPMZZK05AzUQ5VzkR7yA9M05TztiH2Q
"""

# 소수 구하기

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)

# Dynamic Programming 적용..

M, N = map(int, input().split())
dp = [False, False] + [True] * (N-1) # 0,1 은 False, 뒤에는 True로 세팅
primes = []

for i in range(2, N+1):
    if dp[i]:
        for j in range(2*i, N+1, i):
            dp[j] = False

for i in range(M, N+1):
    if dp[i]:
        print(i)