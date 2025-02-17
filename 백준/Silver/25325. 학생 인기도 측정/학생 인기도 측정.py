n = int(input())
d = {}
for a in input().split(): d[a] = 0
for _ in range(n):
    for a in input().split(): d[a] += 1
l = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in l: print(*i)