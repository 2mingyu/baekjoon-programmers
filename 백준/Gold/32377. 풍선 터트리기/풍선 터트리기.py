N, x, y, z = map(int, input().split())
l, r = 1, min(x, y, z)*N
a = r
while l <= r:
    m = (l+r) // 2
    t = m//x + m//y + m//z
    if t >= N:
        a = m
        r = m-1
    elif t < N:
        l = m+1

b = (a-1)//x + (a-1)//y + (a-1)//z

c = []
if a%x == 0: c.append('A')
if a%y == 0: c.append('B')
if a%z == 0: c.append('C')


if c[N-b-1] == 'A': print('A win')
elif c[N-b-1] == 'B': print('B win')
else: print('C win')
