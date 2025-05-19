N, M = map(int, input().split())
A = [[0]*26 for _ in range(M)]
A[0] = [1]*26
for i in range(1, M):
    for j in range(26):
        for k in range(0, j-N+1):
            A[i][j] += A[i-1][k] % 1000000007
        for k in range(j+N, 26):
            A[i][j] += A[i-1][k] % 1000000007
        if N == 0: A[i][j] -= A[i-1][j]
        A[i][j] %= 1000000007
print(sum(A[-1])%1000000007)