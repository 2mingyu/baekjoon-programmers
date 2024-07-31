"""
Cookie Piles
"""
T = int(input())
for _ in range(T):
    N, A, D = map(int, input().split())
    S = 0
    for _ in range(N):
        S += A
        A += D
    print(S)