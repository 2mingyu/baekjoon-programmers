T = int(input())
for t in range(T):
    N = int(input())
    P = [0, 1, 1, 1, 2, 2]
    for n in range(6, N + 1):
        P.append(P[n-1] + P[n-5])
    print(P[N])