"""
The Very Greatest Common Divisor
"""
n = int(input())
for _ in range(n):
    a = int(input())
    b = int(input())
    a, b = (a, b) if a > b else (b, a)
    while b: a, b = b, a % b
    print(a)