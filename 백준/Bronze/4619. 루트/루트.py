while True:
    B, N = map(int, input().split())
    if B == N == 0:
        break

    x = B ** (1 / N)
    a = int(x)

    r = a
    t = abs(a**N - B)

    for i in [a-1, a+1]:
        if i > 0:
            d = abs(i**N - B)
            if d < t:
                t = d
                r = i
    print(r)