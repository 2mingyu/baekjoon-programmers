"""
가장 큰 증가하는 부분 수열
"""
N = int(input())
A = list(map(int, input().split()))
D = A[:]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[j]+A[i], D[i])
print(max(D))