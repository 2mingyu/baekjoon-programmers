n, m = map(int, input().split())
a = [input().split() for _ in range(n)]
for _ in range(m):
    b = input().split()
    r = 0
    for e in a:
        f = 1
        for i in range(3):
            if b[i] != '-' and b[i] != e[i]:
                f = 0
        r += f
    print(r)