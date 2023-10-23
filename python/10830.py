"""
행렬 제곱
mul(n)에서 n=1일때도 나머지 연산 해줘야하네
"""
def square(a, b):
    tmp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += a[i][k]*b[k][j]
            tmp[i][j] %= 1000
    return tmp

N, B = map(int, input().split())
A = []
for _ in range(N): A.append(list(map(int, input().split())))
def mul(n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    tmp = mul(n//2)
    if n%2:
        return square(square(tmp, tmp), A)
    else:
        return square(tmp, tmp)

r = mul(B)
for i in range(N):
    print(*r[i])