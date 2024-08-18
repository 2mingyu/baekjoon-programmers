"""
칠무해
"""
import sys
input = sys.stdin.readline
N = int(input())
l = []
for _ in range(7):
    l.append(float(input()))
l.sort()
for _ in range(7, N):
    l[-1] = min(l[-1], float(input()))
    l.sort()
for i in range(7):
    print('%.3f'%l[i])