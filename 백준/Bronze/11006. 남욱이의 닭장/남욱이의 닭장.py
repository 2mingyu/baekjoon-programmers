T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    T = N - M
    U = M - T
    print(U, T)