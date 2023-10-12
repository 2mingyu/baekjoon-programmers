"""
영역 구하기

예시 그림에서는 왼쪽 아래가 (0,0) 이지만, 리스트 이용할 땐 왼쪽 위를 (0,0) 이라 생각하자
paper에 1로 표시된 곳이 빈 영역
paper에 0으로 표시된 곳이 직사각형 내부
1로 표시된 영역의 수와 넓이를 구하면 됨
"""
import sys
sys.setrecursionlimit(1000000)

def check(y, x):
    if paper[y][x] == 1:
        paper[y][x] = -1
        r = 1
        if y > 0: r += check(y-1, x)
        if x > 0: r += check(y, x-1)
        if y < M-1: r += check(y+1, x)
        if x < N-1: r += check(y, x+1)
        return r
    else:
        return 0

M, N, K = map(int, input().split())
paper = [[1 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 0
r1 = 0
r2 = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 1:
            r1 += 1
            r2.append(check(i, j))
print(r1)
print(" ".join(map(str, sorted(r2))))