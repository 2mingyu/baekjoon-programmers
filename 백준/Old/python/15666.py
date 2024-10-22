"""
N과 M (12)
"""
def f(i):
    if len(s) == M:
        print(*s)
        return
    for j in range(i, N):
        s.append(L[j])
        f(j)
        s.pop()

N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
N, newL = 1, [L[0]]
for l in L[1:]:
    if l != newL[-1]:
        N += 1
        newL.append(l)
L = newL
s = []
f(0)