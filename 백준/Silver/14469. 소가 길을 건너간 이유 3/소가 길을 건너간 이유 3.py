N = int(input())
l = sorted([list(map(int, input().split())) for _ in range(N)])
t = 0
for e in l: t = max(t, e[0]) + e[1]
print(t)