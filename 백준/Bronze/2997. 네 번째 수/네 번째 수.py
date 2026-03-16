a = sorted(map(int, input().split()))
x = a[1] - a[0]
y = a[2] - a[1]

if x == y:
    print(a[2] + x)
elif x < y:
    print(a[1] + x)
else:
    print(a[0] + y)