"""
아기 상어
"""
from collections import deque
N = int(input())
space = []
for _ in range(N): space.append(list(map(int, input().split())))
shark = 2
totalT = 0
eat = 0
sy, sx = -1, -1
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            sy, sx = i, j

def bfs(y, x):
    food = []
    visited = [[0]*N for _ in range(N)]
    q = deque()
    visited[y][x] = 1
    q.append((y, x, 0))
    while q:
        y, x, t = q.popleft()
        for dy, dx in (-1,0), (0,-1), (0,1), (1,0):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    if 0 < space[ny][nx] < shark:
                        food.append((ny, nx, t+1))
                    elif space[ny][nx] == 0 or space[ny][nx] == shark:
                        visited[ny][nx] = 1
                        q.append((ny, nx, t+1))
    return sorted(food, key=lambda x: (x[2], x[0], x[1]))

while True:
    b = bfs(sy, sx)
    if not b: break
    fy, fx, tmpT = b[0]
    totalT += tmpT
    space[sy][sx] = 0
    space[fy][fx] = 9
    sy, sx = fy, fx
    eat += 1
    if eat == shark:
        shark += 1
        eat = 0

print(totalT)