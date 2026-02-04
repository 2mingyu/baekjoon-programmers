while True:
    n = int(input())
    if n == 0: break
    r = 0
    v = list(map(int, input().split()))
    for i in range (1, n-1):
        if v[i] > v[i-1] and v[i] > v[i+1]:
            r += 1
    print(r)