"""
나이트의 이동
"""
from collections import deque

def bfs(x, y):
    visited = set()
    queue = deque([(x, y, 0)])
    visited.add((x, y))
    while queue:
        x, y, depth = queue.popleft()
        if x == x2 and y == y2: return depth
        for dx, dy in  [(1,2), (2,1), (2,-1), (1,-2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and (nx, ny) not in visited:
                queue.append([nx, ny, depth+1])
                visited.add((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(bfs(x1, y1))