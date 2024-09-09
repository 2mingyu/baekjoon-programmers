"""
점 숫자
"""
def f():
    i, j = map(int, input().split())
    a = b = c = d = float('inf')
    z = 1
    n = 1
    while True:
        for x, y in zip(range(1, n+1), range(n, 0, -1)):
            if z == i:
                a, b = y, x
            if z == j:
                c, d = y, x
            if x == b+d and y == a+c:
                print(z)
                return
            z += 1
        n += 1

T = int(input())
for _ in range(T): f()