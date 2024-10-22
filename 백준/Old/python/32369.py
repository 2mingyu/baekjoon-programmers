"""
양파 실험
"""
N, A, B = map(int, input().split())
a = 1
b = 1
for i in range(N):
    a += A
    b += B
    if b > a:
        a, b = b, a
    if a == b:
        b -= 1
print(a, b)
