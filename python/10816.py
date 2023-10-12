"""
숫자 카드 2
"""
import sys
input = sys.stdin.readline
input()
d = dict()
for a in input().split():
    if a in d: d[a] += 1
    else: d[a] = 1
input()
for a in input().split():
    if a in d: print(d[a], end=" ")
    else: print(0, end=" ")