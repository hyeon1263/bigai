# -*- coding: utf-8 -*-
"""백준16953

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SdEFlTXh_pGgItNYreYJwTAA4ANd_Mpi
"""

# A → B

cnt = 0
A, B = map(int, input().split())
while B != A:
    if B % 10 == 1:
        B = B // 10
        cnt += 1
    elif B % 2 == 0:
        B = B // 2
        cnt += 1
    else:
        cnt = -1
        break
    if B < A:
        cnt = -1
        break
if cnt == -1:
    print(cnt)
else:
    print(cnt+1)