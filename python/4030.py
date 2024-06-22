"""
포켓볼
"""
import math
l = []
x = 0
y = 1
while x+1 < 10**9:
    x += y
    y += 1
    z = math.sqrt(x+1)
    if z == int(z):
        l.append(x+1)
n = 1
while True:
    a, b = map(int, input().split())
    if a == b == 0: break
    k = 0
    for ll in l:
        if ll >= b: break
        elif ll > a: k += 1
    print('Case ' + str(n) + ': ' + str(k))
    n += 1