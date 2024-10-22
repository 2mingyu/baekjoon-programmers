"""
소수 구하기
"""
p = [0, 0] + [1] * 1000001
for i in range(2, 1000001):
    ii = i + i
    while ii < 1000001:
        p[ii] = 0
        ii += i
M, N = map(int, input().split())
for i in range(M, N+1):
    if p[i]: print(i)