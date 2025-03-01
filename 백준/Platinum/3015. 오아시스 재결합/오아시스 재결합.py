import sys
input = sys.stdin.readline

N = int(input())
s = []
r = 0

for _ in range(N):
    x = int(input())
    count = 1
    while s and s[-1][0] <= x:
        h, f = s.pop()
        r += f
        if h == x:
            count += f

    if s:
        r += 1

    s.append((x, count))

print(r)
