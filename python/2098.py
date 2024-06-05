"""
외판원 순회
"""
import sys
from collections import deque
input = sys.stdin.readline

inf = float('inf')

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[inf for _ in range(2 ** N)] for _ in range(N)]
r = [inf] * N

dp[0][1] = 0
q = deque([[0, 1]])
while q:
    x, visited = q.popleft()
    if visited == (1 << N) - 1:
        if W[x][0] != 0:
            r[x] = dp[x][visited] + W[x][0]
        else:
            dp[x][visited] = inf
    else:
        for i in range(1, N):
            if W[x][i] != 0 and (visited & (1 << i)) == 0:
                if dp[x][visited] + W[x][i] < dp[i][visited | (1 << i)]:
                    dp[i][visited | (1 << i)] = dp[x][visited] + W[x][i]
                    q.append([i, visited | (1 << i)])

print(min(r))
