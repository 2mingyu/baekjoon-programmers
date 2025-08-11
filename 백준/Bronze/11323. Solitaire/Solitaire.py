T = int(input())
for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    S = 0
    k = [i for i in range(N+1)]
    pk = 0
    pl = 0
    while pk < N:
        if pk + l[pl] <= N:
            pk += l[pl]
            S += k[pk]
        pl = (pl+1)%6
    print(S)