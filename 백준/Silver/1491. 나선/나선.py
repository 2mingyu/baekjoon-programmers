N, M = map(int, input().split())
m = [[0]*N for _ in range(M)]
y = x = i = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(N*M-1):
    m[y][x] = 1
    if 0 <= y+d[i%4][0] < M and 0 <= x+d[i%4][1] < N and not m[y+d[i%4][0]][x+d[i%4][1]]:
        pass
    else:
        i += 1
    y += d[i%4][0]
    x += d[i%4][1]
print(x, y)