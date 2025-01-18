X, Y, P1, P2 = map(int, input().split())
for i in range(1000):
    if P1 == P2:
        print(P1)
        exit()
    if P1 < P2:
        P1 += X
    else:
        P2 += Y
print(-1)