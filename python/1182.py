"""
부분수열의 합
(공집합) 부분수열의 크기가 0 (전부 안 고르는 경우) 을 빼줘야 해서 r-=1
"""
import sys
sys.setrecursionlimit(10**6)
N, S = map(int, input().split())
A = list(map(int, input().split()))
r = 0
def f(s, i):
    global r
    if i == N:
        if s == S: r += 1
        return
    f(s, i+1)
    f(s+A[i], i+1)

f(0, 0)
if S == 0: r -= 1
print(r)