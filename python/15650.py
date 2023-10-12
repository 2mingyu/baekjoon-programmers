"""
N과 M (2)
"""
def f(p, l):
    if len(p) == M:
        for q in p: print(q, end=" ")
        print()
        return
    for i in range(len(l)): f(p+[l[i]], l[i+1:])
N, M = map(int, input().split())
f([], list(range(1, N+1)))