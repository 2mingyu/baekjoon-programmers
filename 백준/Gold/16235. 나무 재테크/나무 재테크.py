N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[5]*N for _ in range(N)]
C = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    C[x-1][y-1].append(z)

for _ in range(K):
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            alive, dead = [], 0
            for age in C[i][j]:
                if age <= B[i][j]:
                    B[i][j] -= age
                    alive.append(age + 1)
                else:
                    dead += age // 2
            C[i][j] = alive
            B[i][j] += dead

    # 가을, 겨울
    new = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for age in C[i][j]:
                if age % 5 == 0:
                    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < N and 0 <= nj < N:
                            new[ni][nj].append(1)

    for i in range(N):
        for j in range(N):
            C[i][j] = new[i][j] + C[i][j]
            B[i][j] += A[i][j]

print(sum(len(C[i][j]) for i in range(N) for j in range(N)))