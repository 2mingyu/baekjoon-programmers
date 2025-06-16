M = int(input())
c = [0, 1, 0, 0]
for _ in range(M):
    X, Y = map(int, input().split())
    c[X], c[Y] = c[Y], c[X]
print(c.index(1))