from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False]*N for _ in range(N)]
q = deque([(r1, c1, 0)])
visited[r1][c1] = True
while q:
    r, c, n = q.popleft()
    if r == r2 and c == c2:
        print(n)
        exit()
    for dr, dc in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            q.append((nr, nc, n+1))
print(-1)