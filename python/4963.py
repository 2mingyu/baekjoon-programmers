"""
섬의 개수
"""
from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and m[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1

while True:
    w, h = map(int, input().split())
    if w == h == 0: break
    m = []
    visited = []
    for _ in range(h):
        m.append(list(map(int, input().split())))
        visited.append([0]*w)
    r = 0
    for y in range(h):
        for x in range(w):
            if not visited[y][x] and m[y][x]:
                r += 1
                bfs(y, x)
    print(r)