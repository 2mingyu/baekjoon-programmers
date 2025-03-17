n = list(map(int, input().split()))
l = [0]
for i in range(4):
    l.append(l[-1] + n[i])

x = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        x[i][j] = abs(l[i] - l[j])

for y in x:
    print(*y)