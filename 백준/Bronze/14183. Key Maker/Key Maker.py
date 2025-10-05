def c(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
    return True

while True:
    m, n = map(int, input().split())
    if m == n == 0: break
    r = 0
    a = list(map(int, input(). split()))
    for _ in range(n):
        b = list(map(int, input().split()))
        r += c(a, b)
    print(r)