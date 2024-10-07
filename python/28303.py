"""
자석

i, k + k, j = i, j
"""
N, K = map(int, input().split())
a = list(map(int, input().split()))

b = [a[i] - a[i+1] - K for i in range(N-1)]
c = [a[i+1] - a[i] - K for i in range(N-1)]

d = [0] * (N-1)
d[0] = b[0]
for i in range(N-2):
    d[i+1] = max(0, d[i]) + b[i+1]
e = [0] * (N-1)
e[0] = c[0]
for i in range(N-2):
    e[i+1] = max(0, e[i]) + c[i+1]


print(max(d+e))