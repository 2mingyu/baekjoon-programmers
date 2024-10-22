"""
쿼드트리
"""
def f(y, x, n):
    global result
    if n == 1:
        result += M[y][x]
        return
    tmp = M[y][x]

    for i in range(y, y+n):
        for j in range(x, x+n):
            if tmp != M[i][j]:
                result += '('
                next_n = n//2
                f(y, x, next_n)
                f(y, x+next_n, next_n)
                f(y+next_n, x, next_n)
                f(y+next_n, x+next_n, next_n)
                result += ')'
                return
    result += tmp
    return

N = int(input())
M = []
for _ in range(N): M.append(input())

result = ''
f(0, 0, N)
print(result)