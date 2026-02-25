n, k = map(int, input().split())
a = 1
for _ in range(n):
    f, r = input().split()
    f = int(f)
    if r == "SAFE":
        if f > a: a = f
    else:
        if f < k: k = f

print(a+1, k-1)