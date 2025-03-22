N = int(input())
for _ in range(N):
    G = int(input())
    s = [int(input()) for _ in range(G)]
    m = 1
    while True:
        if len({e%m for e in s}) == G:
            print(m)
            break
        m += 1