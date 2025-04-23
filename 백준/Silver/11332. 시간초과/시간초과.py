import math

C = int(input())
for _ in range(C):
    S, N, T, L = input().split()
    N, T, L = map(int, [N, T, L])
    X = 0
    if S == 'O(N)': X = N
    elif S == 'O(N^2)': X = N**2
    elif S == 'O(N^3)': X = N**3
    elif S == 'O(2^N)': X = 2**N
    elif S == 'O(N!)': X = math.factorial(N)
    if X * T <= L * 10**8: print('May Pass.')
    else: print('TLE!')