"""
팩토리얼 0의 개수
"""
f=1
for i in range(int(input()),0,-1):f *= i
c=0
for n in str(f)[::-1]:
    if n=='0':c+=1
    else:break
print(c)