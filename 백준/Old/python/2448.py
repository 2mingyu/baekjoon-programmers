"""
별 찍기 - 11
"""
N = int(input())
s = [[' ']*N*2 for _ in range(N)]

def star(t, b, l, r):
    m = (l+r)//2
    if b-t == 3:
        s[t][m] = '*'
        s[t+1][m-1] = s[t+1][m+1] = '*'
        s[t+2][m-2] = s[t+2][m-1] = s[t+2][m] = s[t+2][m+1] = s[t+2][m+2] = '*'
    else:
        star(t, (t+b)//2, (l+m)//2, (m+r)//2)
        star((t+b)//2, b, l, m)
        star((t+b)//2, b, m, r)

top, bottom, left, right = 0, N, 0, N*2-1
star(top, bottom, left, right)

for i in range(N):
    for j in range(N*2):
        print(s[i][j], end="")
    print()