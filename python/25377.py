"""
빵
"""
N = int(input())
r = 1001
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B: r = min(r, B)
if r == 1001: print(-1)
else: print(r)