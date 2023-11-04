"""
치즈
"""
from collections import deque

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    melt = []
    air = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    q = deque()
    visited[0][0] = True
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if space[ny][nx] ==0:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                elif space[ny][nx] == 1:
                    air[ny][nx] += 1
                    if air[ny][nx] == 2:
                        melt.append((ny, nx))
    return melt

t = 0
while True:
    m = bfs()
    if m:
        t += 1
        for my, mx in m:
            space[my][mx] = 0
    else: break
print(t)