"""
수들의 합 2
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
r = 0
i = j = 0
s = A[0]
if s == M: r += 1
while True:
    if s > M:
        s -= A[i]
        i += 1
        if s == M: r += 1
    else:
        j += 1
        if j == N: break
        s += A[j]
        if s == M: r += 1
print(r)