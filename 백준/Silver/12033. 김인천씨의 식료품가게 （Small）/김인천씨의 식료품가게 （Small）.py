T = int(input())

for x in range(1, T + 1):
    N = int(input())
    P = list(map(int, input().split()))

    d = {}
    y = []

    for v in P:
        if d.get(v, 0):
            d[v] -= 1
        else:
            y.append(v)
            d[v * 4 // 3] = d.get(v * 4 // 3, 0) + 1

    print(f"Case #{x}:", *y)