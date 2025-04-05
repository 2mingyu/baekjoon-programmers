T = int(input())
for x in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    m = 0
    r = 0
    for p in reversed(M):
        if p > m:
            m = p
        else:
            r += m-p
    print(f"#{x} {r}")