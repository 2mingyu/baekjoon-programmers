"""
행렬 곱셈 순서
"""
import sys
input = sys.stdin.readline

N = int(input())
m = list(map(int, input().split()))
for _ in range(N-1):
    r, c = map(int, input().split())
    m.append(c)

dp = [[float('inf')]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][i] = 0
for h in range(1, N):
    for i in range(1, N-h+1):
        j = i + h
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + m[i-1]*m[k]*m[j])

print(dp[1][N])