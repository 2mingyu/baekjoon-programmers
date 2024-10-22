"""
단지번호붙이기
"""

def check(y, x):
    if house[y][x] == 1:
        house[y][x] = -1
        r = 1
        if y > 0: r += check(y-1, x)
        if x > 0: r += check(y, x-1)
        if y < N-1: r += check(y+1, x)
        if x < N-1: r += check(y, x+1)
        return r
    else:
        return 0

N = int(input())
house = []
for _ in range(N): house.append(list(map(int, input())))
r1 = 0
r2 = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            r1 += 1
            r2.append(check(i, j))
print(r1)
for rr in sorted(r2): print(rr)