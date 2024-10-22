"""
Bicycle
"""
a, x, b, y, T = [int(input()) for _ in range(5)]
print(a + max(T-30, 0) * x * 21, b + max(T-45, 0) * y * 21)