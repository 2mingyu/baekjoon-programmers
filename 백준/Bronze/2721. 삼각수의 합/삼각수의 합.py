T = int(input())
for i in range(T):
    n = int(input())
    W = 0
    t = 1
    for k in range(1, n+1):
        t += k+1
        W += k*t
    print(W)