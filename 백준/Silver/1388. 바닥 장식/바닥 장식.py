N, M = map(int, input().split())
F = [list(input()) for _ in range(N)]
r = 0
for i in range(N):
    for j in range(M):
        if F[i][j] == '-':
            r += 1
            F[i][j] = '*'
            nj = j+1
            while nj < M and F[i][nj] == '-':
                F[i][nj] = '*'
                nj += 1
        elif F[i][j] == '|':
            r += 1
            F[i][j] = '*'
            ni = i+1
            while ni < N and F[ni][j] == '|':
                F[ni][j] = '*'
                ni += 1
print(r)