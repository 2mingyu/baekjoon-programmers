"""
구간 합 구하기 4

무지성 sum이 아닌 누적합 이용해야함
"""
import sys
N, M = map(int, input().split())
s = [0]
l = list(map(int, input().split()))
for n in l: s.append(n + s[-1])
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(s[j]-s[i-1])