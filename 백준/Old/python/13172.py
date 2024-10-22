"""
Σ
모듈러 역원 b^(-1) = b^(X-2)
"""
import sys
input = sys.stdin.readline
modular = 1000000007
M = int(input())
def get_modular_inverse(n, x):
    if x == 1:
        return n
    tmp = get_modular_inverse(n, x//2)
    if x%2 == 0:
        return tmp * tmp % modular
    else:
        return tmp * tmp * N % modular

result = 0
for i in range(M):
    N, S = map(int, input().split())
    result = (result + S * get_modular_inverse(N, modular-2)) % modular
print(result)