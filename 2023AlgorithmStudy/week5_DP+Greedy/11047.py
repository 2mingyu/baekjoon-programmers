"""

"""
N, K = map(int, input().split())
values = []
result = 0
for _ in range(N): values.insert(0, int(input()))
for v in values:
    result += K // v
    K %= v
print(result)