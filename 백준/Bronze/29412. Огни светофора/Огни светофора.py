g, gb, y, r, ry = map(int, input().split())
T = int(input())
a = b = c = 0
while T:
    c += min(g, T)
    T -= min(g, T)
    if T == 0: break
    c += min(gb, T) // 2
    T -= min(gb, T)
    if T == 0: break
    b += min(y, T)
    T -= min(y, T)
    if T == 0: break
    a += min(r, T)
    T -= min(r, T)
    if T == 0: break
    a += min(ry, T)
    b += min(ry, T)
    T -= min(ry, T)
    if T == 0: break
print(a, b, c)