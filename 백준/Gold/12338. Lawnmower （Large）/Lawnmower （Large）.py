T = int(input())
for x in range(1, T+1):
    N, M = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    max_row = [max(a[i]) for i in range(N)]
    max_col = [max(a[i][j] for i in range(N)) for j in range(M)]
    y = 'YES'
    for i in range(N):
        for j in range(M):
            if a[i][j] < max_row[i] and a[i][j] < max_col[j]:
                y = 'NO'
    print(f"Case #{x}: {y}")