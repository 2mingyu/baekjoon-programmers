"""
Baza
"""
def f():
    for j in range(M):
        if B[j] != -1 and B[j] != D[i][j]:
            return 0
    return 1

N, M = map(int, input().split())
D = []
for _ in range(N):
    A = list(map(int, input().split()))
    D.append(A)
Q = int(input())
for _ in range(Q):
    B = list(map(int, input().split()))
    X = 0
    for i in range(N):
        X += f()
    print(X)