N, G = map(int, input().split())
a = [0] * (N + 1)
e = 1
s = 1
for _ in range(G):
    k = int(input())
    while k:
        while e <= N and a[e] != 0:
            e += 1
        if e <= N:
            x = 2 if k >= 2 else 1
            a[e] = x
            k -= x
            e += 1
        else:
            while s <= N and a[s] != 1:
                s += 1
            a[s] = 2
            k -= 1
for i in range(1, N + 1):
    print(a[i])