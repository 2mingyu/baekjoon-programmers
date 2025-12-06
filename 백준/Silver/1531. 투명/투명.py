N, M = map(int, input().split())
p = [[0]*101 for _ in range(101)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx+1):
        for j in range(ly, ry+1):
            p[i][j] += 1
c = 0
for i in range(1, 101):
    for j in range(1, 101):
        if p[i][j] > M:
            c += 1
print(c)