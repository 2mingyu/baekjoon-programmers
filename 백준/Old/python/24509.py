"""
상품의 주인은?
"""
import sys
input = sys.stdin.readline
N = int(input())
r = []
a = []
b = []
c = []
d = []
for _ in range(N):
    X, A, B, C, D = map(int, input().split())
    if len(a) < 4:
        a.append([X, A])
        a = sorted(a, key=lambda x: (-x[1], x[0]))
    else:
        if A > a[3][1]:
            a.pop()
            a.append([X, A])
        elif A == a[3][1]:
            if X < a[3][0]:
                a.pop()
                a.append([X, A])
        a = sorted(a, key=lambda x: (-x[1], x[0]))
    if len(b) < 4:
        b.append([X, B])
        b = sorted(b, key=lambda x: (-x[1], x[0]))
    else:
        if B > b[3][1]:
            b.pop()
            b.append([X, B])
        elif B == b[3][1]:
            if X < b[3][0]:
                b.pop()
                b.append([X, B])
        b = sorted(b, key=lambda x: (-x[1], x[0]))
    if len(c) < 4:
        c.append([X, C])
        c = sorted(c, key=lambda x: (-x[1], x[0]))
    else:
        if C > c[3][1]:
            c.pop()
            c.append([X, C])
        elif C == c[3][1]:
            if X < c[3][0]:
                c.pop()
                c.append([X, C])
        c = sorted(c, key=lambda x: (-x[1], x[0]))
    if len(d) < 4:
        d.append([X, D])
        d = sorted(d, key=lambda x: (-x[1], x[0]))
    else:
        if D > d[3][1]:
            d.pop()
            d.append([X, D])
        elif D == d[3][1]:
            if X < d[3][0]:
                d.pop()
                d.append([X, D])
        d = sorted(d, key=lambda x: (-x[1], x[0]))
r.append(a[0][0])
for x in b:
    if x[0] not in r:
        r.append(x[0])
        break
for x in c:
    if x[0] not in r:
        r.append(x[0])
        break
for x in d:
    if x[0] not in r:
        r.append(x[0])
        break
print(*r)