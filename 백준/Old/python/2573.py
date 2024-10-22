"""
빙산

c는 빙산 덩어리 개수
"""
from collections import deque

N, M = map(int, input().split())
now = [list(map(int, input().split())) for _ in range(N)]
r = 0
while True:
    c = 0
    visited = [[0] * M for _ in range(N)]
    next = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if now[i][j] != 0 and not visited[i][j]:
                c += 1
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    y, x = q.popleft()
                    next[y][x] = now[y][x]
                    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if now[ny][nx] == 0: next[y][x] = max(0, next[y][x]-1)
                            elif not visited[ny][nx]:
                                visited[ny][nx] = 1
                                q.append((ny, nx))
    now = next
    if c >= 2: print(r); exit()
    if c == 0: print(0); exit()
    r += 1