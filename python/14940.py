"""
쉬운 최단거리 4
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
q = deque([])
v = [[False]*m for _ in range(n)]
r = [[-1]*m for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            q.append((i, j))
            v[i][j] = True
            r[i][j] = 0
        elif tmp[j] == 0:
            r[i][j] = 0
    a.append(tmp)

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()

    for dx, dy in d:
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and a[nx][ny] == 1:
            q.append((nx, ny))
            v[nx][ny] = True
            r[nx][ny] = r[x][y] + 1

# 출력
for i in range(n):
    for j in range(m):
        print(r[i][j], end=" ")
    print()