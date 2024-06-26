"""
사과
"""
N = int(input())
s = 0
for _ in range(N):
    a, b = map(int, input().split())
    s += b%a
print(s)