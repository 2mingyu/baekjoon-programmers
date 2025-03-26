N = int(input())
l = sorted([list(map(int, input().split())) for _ in range(N)])
t = 0
for e in l:
    if e[0] < t:
        t = t + e[1]
    else:
        t = e[0] + e[1]
print(t)