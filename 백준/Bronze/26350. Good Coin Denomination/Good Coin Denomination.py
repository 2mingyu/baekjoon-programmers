n = int(input())
for _ in range(n):
    d, *v = map(int, input().split())
    f = True
    for i in range(1, d):
        if v[i] < v[i-1]*2:
            f = False
    print('Denominations:', *v)
    print(['Bad', 'Good'][f], 'coin denominations!\n')