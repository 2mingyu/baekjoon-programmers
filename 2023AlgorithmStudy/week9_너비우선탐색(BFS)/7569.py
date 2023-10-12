"""
토마토
"""
from collections import deque

def bfs():
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1: queue.append([h, n, m])
    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]:
            nz, ny, nx = z+dz, y+dy, x+dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and not tomato[nz][ny][nx]:
                queue.append([nz, ny, nx])
                tomato[nz][ny][nx] = tomato[z][y][x] + 1

M, N, H = map(int, input().split())
tomato = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        tomato[h][n] = (list(map(int, input().split())))
bfs()
result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:
                print(-1)
                exit(0)
        result = max(result, max(tomato[h][n]))
print(result - 1)
