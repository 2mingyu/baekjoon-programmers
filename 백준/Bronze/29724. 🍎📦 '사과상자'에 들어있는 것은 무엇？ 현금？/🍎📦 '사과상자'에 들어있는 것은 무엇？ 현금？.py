N = int(input())
g = 0
c = 0
for _ in range(N):
    T, W, H, L = input().split()
    W, H, L = map(int, (W, H, L))
    if T == 'A':
        n = (W//12) * (H//12) * (L//12)
        g += 1000 + n*500
        c += n*4000
    elif T == 'B':
        g += 50 * 120
print(g)
print(c)