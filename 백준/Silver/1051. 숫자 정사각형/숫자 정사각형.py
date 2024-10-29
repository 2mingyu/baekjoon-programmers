N, M = map(int, input().split())
l = [input() for _ in range(N)]
r = 1
for i in range(N):
    for j in range(M):
        y, x = i+1, j+1
        while y < N and x < M:
            if l[i][j] == l[i][x] == l[y][j] == l[y][x]:
                r = max(r, (y-i+1)**2)
            y += 1
            x += 1
print(r)