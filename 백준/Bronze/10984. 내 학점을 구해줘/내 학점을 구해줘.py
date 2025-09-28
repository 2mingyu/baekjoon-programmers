T = int(input())
for _ in range(T):
    N = int(input())
    sC = sG = 0
    for _ in range(N):
        C, G = map(float, input().split())
        sC += int(C)
        sG += C*G
    print(sC, round(sG/sC, 1))