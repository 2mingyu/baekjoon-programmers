A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())
for t in [P, M, N]:
    t -= 1
    r = 0
    if t % (A + B) < A: r += 1
    if t % (C + D) < C: r += 1
    print(r)