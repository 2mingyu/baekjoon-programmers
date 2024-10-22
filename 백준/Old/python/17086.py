"""
아기 상어 2

아 처음에 문제를 잘못 이해함.
상어와 상어 사이 거리가 안전거리인줄
"""
from collections import deque

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
safe = [[float('inf')]*M for _ in range(N)]
s = deque()
for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            s.append((i, j))
            safe[i][j] = 0


def bfs(a, b):
    q = deque()
    visited = [[False]*M for _ in range(N)]
    q.append((a, b, 0))
    visited[a][b] = True
    while q:
        y, x, n = q.popleft()
        for dy, dx in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                safe[ny][nx] = min(safe[ny][nx], n+1)
                q.append((ny, nx, n+1))
                visited[ny][nx] = True


while s:
    a, b = s.popleft()
    bfs(a, b)
r = 0
for s in safe:
    r = max(r, max(s))
print(r)