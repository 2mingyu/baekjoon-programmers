N = int(input())
r = [float('inf'), float('inf')]
for _ in range(N):
    x, y = map(int, input().split())
    if y < r[1]:
        r = [x, y]
print(r[0], r[1])