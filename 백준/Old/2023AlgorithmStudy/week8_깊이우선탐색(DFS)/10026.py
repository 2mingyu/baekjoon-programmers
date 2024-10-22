"""
적록색약
"""
import sys
sys.setrecursionlimit(10000000)

def check(c, y, x, z):
    if c[y][x] == z:
        c[y][x] = 'C'
        if y > 0: check(c, y-1, x, z)
        if x > 0: check(c, y, x-1, z)
        if y < N-1: check(c, y+1, x, z)
        if x < N-1: check(c, y, x+1, z)

N = int(input())
color = [list(map(str, input())) for _ in range(N)]
weaknessColor = []
for c in color:
    tmp = []
    for cc in c:
        if cc == 'G': tmp.append('R')
        else: tmp.append(cc)
    weaknessColor.append(tmp)
notWeakness = 0
weakness = 0
for i in range(N):
    for j in range(N):
        if color[i][j] != 'C':
            notWeakness += 1
            check(color, i, j, color[i][j])
for i in range(N):
    for j in range(N):
        if weaknessColor[i][j] != 'C':
            weakness += 1
            check(weaknessColor, i, j, weaknessColor[i][j])
print(notWeakness)
print(weakness)