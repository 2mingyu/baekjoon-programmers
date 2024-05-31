"""
Triathlon
"""
N = int(input())
r = 0
for _ in range(N):
    a, d, g = map(int, input().split())
    t = a * (d + g)
    if a == d + g: t *= 2
    r = max(r, t)
print(r)