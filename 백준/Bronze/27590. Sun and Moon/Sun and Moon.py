ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
s = -ds
m = -dm
while s != m:
    if s < m:
        s += ys
    else:
        m += ym
print(s)