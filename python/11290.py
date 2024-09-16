"""
Wonowon
"""
def W(x):
    w = 101
    for i in range(3, x, 2):
        if w % x == 0:
            return i
        w = (100 * w + 1) % x
    return -1

n = int(input())
primes = []
t = [1 for _ in range(n+1)]
t[0] = t[1] = 0
for i in range(n+1):
    if t[i]:
        primes.append(i)
        for j in range(i+i, n+1, i):
            t[j] = 0
r = 0
for p in primes:
    if W(p) == p - 2:
        r += 1
print(r)