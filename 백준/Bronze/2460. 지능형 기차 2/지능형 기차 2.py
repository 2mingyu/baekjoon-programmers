m = 0
r = 0
for _ in range(10):
    a, b = map(int, input().split())
    r = r-a+b
    m = max(m, r)
print(m)