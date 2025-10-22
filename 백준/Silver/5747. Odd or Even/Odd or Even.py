while True:
    N = int(input())
    if not N: break
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    ox = ex = ey = oy = 0
    for e in X:
        if e%2: ox += 1
        else: ex += 1
    for e in Y:
        if e%2: oy += 1
        else: ey += 1
    print(N-min(ox, ey)-min(oy, ex))