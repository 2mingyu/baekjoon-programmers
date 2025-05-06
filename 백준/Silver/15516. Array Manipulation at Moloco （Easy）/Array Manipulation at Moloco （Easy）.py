n = int(input())
A = [int(input()) for _ in range(n)]
S = [0] * n
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            S[i] += 1
print(*S, sep='\n')