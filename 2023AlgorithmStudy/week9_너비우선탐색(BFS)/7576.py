"""
토마토
"""
from collections import deque

def bfs():
    queue = deque()
    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 1: queue.append([n, m])
    while queue:
        y, x = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < M and 0 <= ny < N and not tomato[ny][nx]:
                queue.append([ny, nx])
                tomato[ny][nx] = tomato[y][x] + 1

M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))
bfs()
result = 0
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 0:
            print(-1)
            exit(0)
    result = max(result, max(tomato[n]))
print(result - 1)