"""
팰린드롬?

S부터 E까지 팰린드롬이면 S+1부터 E-1까지도 팰린드롬
https://4z7l.github.io/2021/04/07/algorithms-boj-10942.html

1 3
2 4
3 5
4 6
5 7
1 4
2 5
3 6
4 7

"""
import sys
input = sys.stdin.readline

N = int(input())
A = [-1] + list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1): dp[i][i] = 1
for i in range(1, N):
    if A[i] == A[i+1]: dp[i][i+1] = 1
for i in range(2, N):
    s = 1
    e = s+i
    while True:
        if A[s] == A[e] and dp[s+1][e-1]:
            dp[s][e] = 1
        s += 1
        e += 1
        if e > N: break

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])