"""
피보나치 수 6
10830 행렬 제곱과 유사
[[F[n]], F[n-1]] = [[1, 1], [1, 0]] * [[F[n-1]], F[n-2]]
"""
import sys
sys.setrecursionlimit(10000000)
N = int(input())
A = [[1, 1], [1, 0]]
def square(a, b):
    tmp = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += a[i][k]*b[k][j]
            tmp[i][j] %= 1000000007
    return tmp
def mul(n):
    if n == 1:
        return A
    tmp = mul(n//2)
    if n%2:
        return square(square(tmp, tmp), A)
    else:
        return square(tmp, tmp)

r = mul(N)
print(r[0][1]%1000000007)