"""
Pizza Boxes
"""
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
sm = [max(r) for r in l]
fm = [max(c) for c in zip(*l)]
r = 0
for i in range(n):
    for j in range(m):
        if l[i][j] < sm[i] and l[i][j] < fm[j]:
            r += l[i][j]
print(r)