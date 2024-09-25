"""
스파이
"""
def f(p, s, n):
    global r
    if n == 0:
        if s >= M:
            r += 1
        return
    for i in range(6):
        if i == p or i == p+3 or i == p-3:
            f(i, s+l[i]//2, n-1)
        else:
            f(i, s+l[i], n-1)

N, M = map(int, input().split())
l = list(map(int, input().split())) + list(map(int, input().split()))
r = 0
f(9, 0, N)
print(r)