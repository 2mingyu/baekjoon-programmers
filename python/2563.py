"""
색종이
"""
p = [[0]*100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            p[i][j] = 1
r = 0
for i in range(100):
    r += sum(p[i])
print(r)