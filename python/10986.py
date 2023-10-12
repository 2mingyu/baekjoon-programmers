"""
나머지 합
https://banwolcode.tistory.com/47
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(1, N): A[i] += A[i-1]
C = [0] * M
for i in range(N): C[A[i]%M] += 1
result = C[0]
for c in C: result += (c*(c-1))//2
print(result)