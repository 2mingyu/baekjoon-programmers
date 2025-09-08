N, M = map(int, input().split())
A = [int(input()) for i in range(N)]
B = [int(input()) for j in range(M)]
C = [0]*N
for j in range(M):
    for i in range(N):
        if A[i] <= B[j]:
            C[i] += 1
            break
print(C.index(max(C))+1)