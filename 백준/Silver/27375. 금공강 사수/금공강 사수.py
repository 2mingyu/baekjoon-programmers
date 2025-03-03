def check(a, b):
    for c in b:
        if a[0] == c[0] and (a[1] <= c[1] <= a[2] or a[1] <= c[2] <= a[2] or c[1] <= a[1] <= c[2] or c[1] <= a[2] <= c[2]):
            return False
    return True

def f(idx, ll, kk):
    global r
    if kk == 0:
        r += 1
        return
    for i in range(idx, len(l)):
        if check(l[i], ll):
            f(i+1, ll+[l[i]], kk-l[i][3])

r = 0
n, k = map(int, input().split())
l = []
for _ in range(n):
    w, s, e = map(int, input().split())
    if w != 5:
        l.append([w, s, e, e-s+1])
f(0, [], k)
print(r)