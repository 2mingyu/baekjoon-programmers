"""
미로 탐색
"""
from collections import deque

def bfs():
    visited = set()
    queue = deque()
    visited.add((0,0))
    queue.append([0,0,1])
    while queue:
        y, x, depth = queue.popleft()
        for dy, dx in [(1,0), (0,1), (-1,0), (0,-1)]:
            ny, nx = y+dy, x+dx
            if ny == N-1 and nx == M-1: return depth+1
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in visited and maze[ny][nx]:
                queue.append([ny, nx, depth+1])
                visited.add((ny, nx))

N, M = map(int, input().split())
maze = []
for _ in range(N): maze.append(list(map(int, input())))
print(bfs())