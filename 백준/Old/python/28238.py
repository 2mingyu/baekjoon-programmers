"""
정보 선생님의 야망
"""
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
r1 = r2 = r3 = 0
for x in range(4):
    for y in range(x+1, 5):
        z = 0
        for i in range(n):
            if a[i][x] and a[i][y]:
                z += 1
        if z >= r3:
            r1, r2, r3 = x, y, z
print(r3)
print(*[int(i in [r1, r2]) for i in range(5)])