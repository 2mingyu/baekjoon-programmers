"""
말이 되고픈 원숭이

c 는 count
"""
from collections import deque

K = int(input())
W, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

q = deque([(0, 0, 0)])
visited[0][0][0] = 1
while q:
    y, x, k = q.popleft()
    if y == H-1 and x == W-1:
        print(visited[y][x][k]-1)
        exit(0)
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][k] and not A[ny][nx]:
            q.append((ny, nx, k))
            visited[ny][nx][k] = visited[y][x][k] + 1
    if k < K:
        for dy, dx in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx][k+1] and not A[ny][nx]:
                q.append((ny, nx, k+1))
                visited[ny][nx][k+1] = visited[y][x][k] + 1
print(-1)