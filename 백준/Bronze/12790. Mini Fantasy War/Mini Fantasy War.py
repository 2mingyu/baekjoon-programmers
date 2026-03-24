t = int(input())
for _ in range(t):
    h, m, a, d, x, y, z, w = map(int, input().split())

    h += x
    m += y
    a += z
    d += w

    if h < 1: h = 1
    if m < 1: m = 1
    if a < 0: a = 0

    r = h + 5*m + 2*a + 2*d
    print(r)