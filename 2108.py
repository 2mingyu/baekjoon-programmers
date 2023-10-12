"""
통계학
"""
import sys
input = sys.stdin.readline
N = int(input())
l = sorted([int(input()) for _ in range(N)])
print(round(sum(l)/N))
print(l[N//2])
d = dict()
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
ll = []
maxCount = 0
for i in d:
    if d[i] > maxCount:
        ll = [i]
        maxCount = d[i]
    elif d[i] == maxCount:
        ll.append(i)
if len(ll) > 1: print(ll[1])
else: print(ll[0])
print(l[-1]-l[0])