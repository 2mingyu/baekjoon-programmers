"""
Dangerous Dive
"""
N, R = map(int, input().split())
A = [0]*(N+1)
B = list(map(int, input().split()))
for i in range(R):
    A[B[i]] = 1
C = []
for i in range(1, N+1):
    if not A[i]:
        C.append(i)
if C:
    print(' '.join(map(str, C)))
else:
    print('*')