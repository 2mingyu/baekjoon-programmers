from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    v[y][x] = True
    z = 1
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < 3 and 0 <= nx < 3 and m[ny][nx] == 'O' and not v[ny][nx]:
                q.append((ny, nx))
                z += 1
                v[ny][nx] = True
    return z


T = int(input())
for _ in range(T):
    v = [[False]*3 for _ in range(3)]
    m = [input() for _ in range(3)]
    n, *a = map(int, input().split())
    b = []
    for i in range(3):
        for j in range(3):
            if m[i][j] == 'O' and not v[i][j]:
                c = bfs(i, j)
                if c: b.append(c)
    print(int(sorted(a) == sorted(b)))
