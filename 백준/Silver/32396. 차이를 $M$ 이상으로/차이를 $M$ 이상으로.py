N, M = map(int, input().split())
A = list(map(int, input().split()))
r = 0
for i in range(1, N):
    if abs(A[i] - A[i-1]) < M:
        r += 1
        A[i] = float('inf')
print(r)