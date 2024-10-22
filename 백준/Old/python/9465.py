"""
스티커
dp[j][i] = max(dp[not j][i-1], dp[not j][i-2]) + l[j][i]
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0]*(n+1) for _ in range(2)]
    l = []
    l.append([0] + list(map(int, input().split())))
    l.append([0] + list(map(int, input().split())))
    dp[0][1] = l[0][1]
    dp[1][1] = l[1][1]
    for i in range(2, n+1):
        for j in 0, 1:
            dp[j][i] = max(dp[not j][i-1], dp[not j][i-2]) + l[j][i]
    print(max(dp[0][n], dp[1][n], dp[0][n-1], dp[1][n-1]))