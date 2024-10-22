"""
내리막 길
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def f(y, x):
    if y == M-1 and x == N-1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    H = 0
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < M and 0 <= nx < N:
            if A[y][x] > A[ny][nx]:
                H += f(ny, nx)
    dp[y][x] = H
    return dp[y][x]

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
print(f(0, 0))