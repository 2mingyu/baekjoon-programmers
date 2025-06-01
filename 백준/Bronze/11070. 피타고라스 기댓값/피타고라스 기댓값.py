T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    t = [[0, 0] for _ in range(n+1)]
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        t[a][0] += p
        t[a][1] += q
        t[b][0] += q
        t[b][1] += p
    w = [0]*(n+1)
    for i in range(n+1):
        if t[i][0] != 0 or t[i][1] != 0:
            w[i] = t[i][0]**2 / (t[i][0]**2 + t[i][1]**2)
    print(int(max(w[1:])*1000))
    print(int(min(w[1:])*1000))