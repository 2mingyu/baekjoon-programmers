N, M = map(int, input().split())
l = [[0]*(M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(M+2)]

n = 1
for i in range(1, N+1):
    l[i][0] = n
    n += 1
for i in range(1, M+1):
    l[N+1][i] = n
    n += 1
for i in range(N, 0, -1):
    l[i][M+1] = n
    n += 1
for i in range(M, 0, -1):
    l[0][i] = n
    n += 1

for i in range(1, N+1):
    d = 'r'
    ny, nx = i, 1
    while 0 < ny < N+1 and 0 < nx < M+1:
        if l[ny][nx]:
            if d == 'r': d = 'u'
            elif d == 'u': d = 'r'
        if d == 'r':
            ny, nx = ny, nx+1
        elif d == 'u':
            ny, nx = ny-1, nx
    print(l[ny][nx], end=' ')
for i in range(1, M+1):
    d = 'u'
    ny, nx = N, i
    while 0 < ny < N+1 and 0 < nx < M+1:
        if l[ny][nx]:
            if d == 'r': d = 'u'
            elif d == 'u': d = 'r'
        if d == 'r':
            ny, nx = ny, nx+1
        elif d == 'u':
            ny, nx = ny-1, nx
    print(l[ny][nx], end=' ')
for i in range(N, 0, -1):
    d = 'l'
    ny, nx = i, M
    while 0 < ny < N+1 and 0 < nx < M+1:
        if l[ny][nx]:
            if d == 'l': d = 'd'
            elif d == 'd': d = 'l'
        if d == 'l':
            ny, nx = ny, nx-1
        elif d == 'd':
            ny, nx = ny+1, nx
    print(l[ny][nx], end=' ')
for i in range(M, 0, -1):
    d = 'd'
    ny, nx = 1, i
    while 0 < ny < N+1 and 0 < nx < M+1:
        if l[ny][nx]:
            if d == 'l': d = 'd'
            elif d == 'd': d = 'l'
        if d == 'l':
            ny, nx = ny, nx-1
        elif d == 'd':
            ny, nx = ny+1, nx
    print(l[ny][nx], end=' ')