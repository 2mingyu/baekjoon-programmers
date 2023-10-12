"""
카잉 달력
마지막 해는 M, N의 최소공배수?
k = M * a + x = N * b + y
M * a - N * b = y - x 를 만족하는 a, b가 있어야 함?
없으면 k = -1
a >= 0, b >= 0
"""
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(int(input())):
    M, N, x, y = map(int ,input().split())
    k = x
    l = lcm(M, N)
    while k <= l:
        if (k-y) % N == 0:
            print(k)
            break
        k += M
    if k > l:
        print(-1)