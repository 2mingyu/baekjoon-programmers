"""
종이의 개수
"""
def f(l, t, n):
    v = p[l][t]
    if n == 1:
        r[int(v)] += 1
        return
    m = n//3
    for i in range(l, l+n):
        for j in range(t, t+n):
            if p[i][j] != v:
                f(l, t, m)
                f(l+m, t, m)
                f(l+m+m, t, m)
                f(l, t+m, m)
                f(l+m, t+m, m)
                f(l+m+m, t+m, m)
                f(l, t+m+m, m)
                f(l+m, t+m+m, m)
                f(l+m+m, t+m+m, m)
                return
    r[int(v)] += 1
    return

N = int(input())
r = [0, 0, 0]
p = [input().split() for _ in range(N)]
f(0, 0, N)
print(r[-1])
print(r[0])
print(r[1])