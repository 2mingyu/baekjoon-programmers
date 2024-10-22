"""
음식물 피하기
"""
import sys
sys.setrecursionlimit(1000000)

def check(y, x):
    if prog[y][x] == 1:
        prog[y][x] = -1
        s = 1
        if y > 0: s += check(y-1, x)
        if x > 0: s += check(y, x-1)
        if y < N-1: s += check(y+1, x)
        if x < M-1: s += check(y, x+1)
        return s
    else:
        return 0

N, M, K = map(int, input().split())
prog = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    prog[r-1][c-1] = 1
maxSize = 0
for i in range(N):
    for j in range(M):
        if prog[i][j] == 1:
            size = check(i, j)
            maxSize = max(maxSize, size)
print(maxSize)