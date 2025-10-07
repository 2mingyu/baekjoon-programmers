N = int(input())
f = [float(input()) for _ in range(N)]
a = sum(f) / max(N, 1)
r = 0
for e in f:
    if abs(e-a) > 10.0:
        r += 1
print(r)