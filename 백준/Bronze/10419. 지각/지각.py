T = int(input())
for _ in range(T):
    d = int(input())
    t = 0
    while (t + 1) + (t + 1) ** 2 <= d:
        t += 1
    print(t)