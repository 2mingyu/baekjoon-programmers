"""
로봇
"""
M, n = map(int, input().split())
p = [0, 0]
l = 0
for _ in range(n):
    c, d = input().split()
    d = int(d)
    if c == 'TURN':
        if d == 0:
            l = (l-1)%4
        elif d == 1:
            l = (l+1)%4
    elif c == 'MOVE':
        if l == 0:
            p[0] += d
        elif l == 1:
            p[1] -= d
        elif l == 2:
            p[0] -= d
        elif l == 3:
            p[1] += d
        if not (0 <= p[0] <= M and 0 <= p[1] <= M):
            print(-1)
            exit()
print(p[0], p[1])