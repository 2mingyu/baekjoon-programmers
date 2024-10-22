"""
색종이 만들기
"""
def f(n, t, b, l, r):
    if n == 1:
        if p[t][l]: wb[1] += 1
        else: wb[0] += 1
        return
    s = 0
    for i in range(t, b):
        for j in range(l, r):
            s += p[i][j]
    if s == 0:
        wb[0] += 1
        return
    elif s == n*n:
        wb[1] += 1
        return
    else:
        f(n//2, t, (t+b)//2, l, (l+r)//2)
        f(n//2, t, (t+b)//2, (l+r)//2, r)
        f(n//2, (t+b)//2, b, l, (l+r)//2)
        f(n//2, (t+b)//2, b, (l+r)//2, r)

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
wb = [0, 0]
f(N, 0, N, 0, N)
print(wb[0])
print(wb[1])