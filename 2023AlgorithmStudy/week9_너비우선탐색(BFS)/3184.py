"""
양
"""
from collections import deque

def bfs(y, x):
    queue = deque()
    visited.add((y, x))
    queue.append([y, x])
    s = 0
    w = 0
    while queue:
        y, x = queue.popleft()
        if yard[y][x] == 'o': s += 1
        elif yard[y][x] == 'v': w += 1
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C and (ny, nx) not in visited and yard[ny][nx] != '#':
                queue.append([ny, nx])
                visited.add((ny, nx))
    return s, w

R, C = map(int, input().split())
yard = []
for _ in range(R): yard.append(list(input()))
visited = set()
sheep = 0
wolf = 0
for r in range(R):
    for c in range(C):
        if (r, c) not in visited and yard[r][c] != '#':
            tmp_sheep, tmp_wolf = bfs(r, c)
            if tmp_sheep > tmp_wolf: sheep += tmp_sheep
            else: wolf += tmp_wolf
print(sheep, wolf)