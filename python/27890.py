"""
특별한 작은 분수
"""
x, N = map(int, input().split())
for i in range(N):
    if x%2: x = (x*2)^6
    else: x = (x//2)^6
print(x)