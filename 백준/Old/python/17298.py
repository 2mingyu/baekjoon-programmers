"""
오큰수

https://cocoon1787.tistory.com/347
"""
N = int(input())
A = list(map(int, input().split()))
S = []
NGE = [-1] * N
for i in range(N-1, -1, -1):
    while S and S[-1] <= A[i]: S.pop()
    if not S: NGE[i] = -1
    else: NGE[i] = S[-1]
    S.append(A[i])
print(*NGE)