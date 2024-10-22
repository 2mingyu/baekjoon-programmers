"""
유기농 배추
sys.setrecursionlimit : 최대 재귀 깊이 변경
sys.getrecursionlimit : 최대 재귀 깊이 확인
"""
import sys
sys.setrecursionlimit(10000)

def check(y, x, nn):
    if cabbage[y][x] == 1 and checked[y][x] == 0:
        checked[y][x] = nn
        if y > 0:
            check(y-1, x, nn)
        if x > 0:
            check(y, x-1, nn)
        if y < N-1:
            check(y+1, x, nn)
        if x < M-1:
            check(y, x+1, nn)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage[Y][X] = 1
    checked = [[0 for _ in range(M)] for _ in range(N)]
    n = 1
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and checked[i][j] == 0:
                check(i, j, n)
                n += 1
    print(n-1)