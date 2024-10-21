"""
Fold the Paper Nicely
"""
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    print('Data set:', a, b, c)
    for _ in range(c):
        if b > a: a, b = b, a
        a //= 2
    if b > a: a, b = b, a
    print(a, b)
    print()