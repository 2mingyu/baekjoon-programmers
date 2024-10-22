"""
파스칼 삼각형
"""
R, C, W = map(int, input().split())
l = [[1]]
for i in range(1, R+W-1):
    t = [1]
    for j in range(1, i):
        t.append(l[i-1][j-1] + l[i-1][j])
    t.append(1)
    l.append(t)
r = 0
for i in range(R-1, R+W-1):
    for j in range(C-1, C+i-R+1):
        r += l[i][j]
print(r)