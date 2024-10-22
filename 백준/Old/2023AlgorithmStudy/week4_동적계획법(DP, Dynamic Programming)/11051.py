"""
nCk = (n,k) 라고 하자
(n,k) = (n-1,k) + (n-1,k-1)
(1,0) = (1,1) = (n,0) = (n,n) = 1
"""

N, K = map(int, input().split())
C = [0, [1, 1]]
for i in range(2, N + 1):
    tmpC = [1]
    for j in range(1, i):
        tmpC.append((C[i-1][j] + C[i-1][j-1]) % 10007)
    tmpC.append(1)
    C.append(tmpC)
print(C[N][K])