"""
이항 계수 1
"""
N, K = map(int, input().split())
r = 1
for i in range(N-K+1, N+1): r *= i
for i in range(1, K+1): r //= i
print(r)