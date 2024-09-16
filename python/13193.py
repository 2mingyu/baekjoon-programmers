"""
Router 2
N, M, P = map(int, input().split())
print(2*N, N*N)
for i in range(1, N+1):
    for j in range(1, N+1):
        print(i, j+N)
"""
N=223
print(2*N,N*N)
for i in range(N):
 for j in range(N):print(i+1,N+j+1)