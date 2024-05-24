"""
선물
"""
N, X = map(int, input().split())
A = list(map(int, input().split()))
r = float('inf')
for i in range(N-1):
    r = min(A[i]+A[i+1], r)
print(r*X)