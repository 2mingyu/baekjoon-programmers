"""
별 찍기 - 10
"""
def f(y, x, n, mid):
    if mid:
        for i in range(y, y+n):
            for j in range(x, x+n):
                r[i][j] = ' '
    else:
        if n == 3:
            r[y+1][x+1] = ' '
        else:
            d = n//3
            f(y, x, d, False)
            f(y, x+d, d, False)
            f(y, x+d+d, d, False)
            f(y+d, x, d, False)
            f(y+d, x+d, d, True)
            f(y+d, x+d+d, d, False)
            f(y+d+d, x, d, False)
            f(y+d+d, x+d, d, False)
            f(y+d+d, x+d+d, d, False)

N = int(input())
r = [['*']*N for _ in range(N)]
f(0, 0, N, False)
for i in range(N):
    for j in range(N):
        print(r[i][j], end="")
    print()