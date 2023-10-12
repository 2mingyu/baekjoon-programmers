"""
안전 영역
잠기면 0, 안잠기면 1
1의 영역 개수 구하기
"""
import sys
sys.setrecursionlimit(10000000)

def check(y, x):
    if flooded[y][x] == 1:
        flooded[y][x] = -1
        if y > 0: check(y-1, x)
        if x > 0: check(y, x-1)
        if y < N-1: check(y+1, x)
        if x < N-1: check(y, x+1)

N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]
maxSafe = 0
for h in range(1, 101):
    flooded = [[1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if h > height[i][j]:
                flooded[i][j] =  0
    safe = 0
    for i in range(N):
        for j in range(N):
            if flooded[i][j] == 1:
                safe += 1
                check(i, j)
    if safe == 0: break
    if safe > maxSafe: maxSafe = safe
print(maxSafe)