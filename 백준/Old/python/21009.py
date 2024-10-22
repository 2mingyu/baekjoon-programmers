"""
Visible Trees
"""
N = int(input())
l = [[int(x) for x in input().split()] for _ in range(N)]
rl = []
for j in range(N):
    r = m = 0
    for i in range(N):
        if l[i][j] > m:
            m = l[i][j]
            r += 1
    rl.append(r)
print(*rl)
for i in range(N):
    r = m = 0
    for j in range(N):
        if l[i][j] > m:
            m = l[i][j]
            r += 1
    print(r)