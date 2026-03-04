import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

v = [
    (a*d + b*c, c*d),
    (c*b + a*d, d*b),
    (d*a + c*b, b*a),
    (b*c + d*a, a*c)
]

bi = 0
bp, bq = v[0]

for i in range(1, 4):
    p, q = v[i]
    if p * bq > bp * q:
        bi = i
        bp, bq = p, q

print(bi)