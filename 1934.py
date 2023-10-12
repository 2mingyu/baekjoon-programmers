"""
최소공배수

유클리드 호제법?
"""
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(lcm(A, B))