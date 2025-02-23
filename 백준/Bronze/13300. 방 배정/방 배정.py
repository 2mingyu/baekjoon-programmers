N, K = map(int, input().split())
l = [[0]*6, [0]*6]
for _ in range(N):
    S, Y = map(int, input().split())
    l[S][Y-1] += 1
r = 0
for i in range(2):
    for j in range(6):
        r += l[i][j]//K + bool(l[i][j]%K)
print(r)