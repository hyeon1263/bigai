# -*- coding: utf-8 -*-
"""백준9020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JgycT7pedlAp0sZ-Jr6u7AjU_npc2mA-
"""

# 골드바흐의 추측

# prime list를 이용해서 짠 코드 (시간초과!)
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

def primeList(num):
    p_list = []
    for i in range(2,num):
        if isPrime(i) == True:
            p_list.append(i)
    return p_list

T = int(input())
for i in range(T):
    n = int(input())
    n_list = primeList(n)
    
    min_gap = n
    for j in range(len(n_list)):
        if n - n_list[j] in n_list:
            if min_gap > abs(n-2*n_list[j]):
                min_gap = abs(n-2*n_list[j])
                min1 = n_list[j]
                min2 = n-n_list[j]

    print(min(min1,min2), max(min1,min2))

# list 사용없이
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    
    for j in range(n//2):
        center = n//2
        front = center - j
        back = center + j
        if isPrime(front) and isPrime(back):
            print(front, back)
            break