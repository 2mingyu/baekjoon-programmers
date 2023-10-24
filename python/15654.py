"""
N과 M (5)
"""
def f(p, m):
    if m == 0:
        print(*p)
        return
    for a in l:
        if a not in p:
            f(p+[a], m-1)
N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
f([], M)