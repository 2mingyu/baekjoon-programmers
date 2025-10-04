n = int(input())
a = list(map(int ,input().split()))
x = int(input())
a.sort()
i, j = 0, n-1
r = 0
while i < j:
    s = a[i] + a[j]
    if s == x:
        r += 1
    if s > x:
        j -= 1
    else:
        i += 1
print(r)