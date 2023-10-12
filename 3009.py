"""
네 번째 점
"""
a = []
xy = [0, 0]
for _ in range(3):
    a.append(list(map(int,input().split())))
for i in (0, 1):
    if a[0][i] == a[1][i]: xy[i] = a[2][i]
    elif a[0][i] == a[2][i]: xy[i] = a[1][i]
    elif a[1][i] == a[2][i]: xy[i] = a[0][i]
print(' '.join(map(str, xy)))