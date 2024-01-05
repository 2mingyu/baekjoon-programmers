"""
인구 이동
"""
from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def bfs(py, px):
    q = deque([(py, px)])
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(A[ny][nx] - A[y][x]) <= R:
                    union.append((ny, nx))
                    visited[ny][nx] = True
                    q.append((ny, nx))

day = 0
while True:
    temp = False
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = [(i, j)]
                visited[i][j] = True
                bfs(i, j)
                if len(union) > 1:
                    temp = True
                    people = sum(A[y][x] for y, x in union) // len(union)
                    for y, x in union: A[y][x] = people

    if not temp: break
    day += 1

print(day)