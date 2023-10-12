"""
수 정렬하기 3
"""
import sys
input=sys.stdin.readline
a=[0]*10001
for _ in range(int(input())):a[int(input())]+=1
for i in range(10001):
    for _ in range(a[i]):print(i)