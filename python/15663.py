"""
N과 M (5)
"""
def f(p, l, m):
    if m == 0:
        print(*p)
        return
    for i in range(len(l)):
        if i == 0 or l[i] != l[i-1]:
            f(p+[l[i]], l[:i]+l[i+1:], m-1)
N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
f([], l, M)