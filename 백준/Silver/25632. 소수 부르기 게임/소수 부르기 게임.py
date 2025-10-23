p = [1]*1001
for i in range(2, 1001):
    if p[i]:
        for j in range(i*2, 1001, i):
            p[j] = 0
A, B = map(int, input().split())
C, D = map(int, input().split())
yt = set()
yj = set()
both = set()
for i in range(2, 1001):
    if p[i]:
        if A <= i <= B: yt.add(i)
        if C <= i <= D: yj.add(i)
        if A <= i <= B and C <= i <= D: both.add(i)
turn = len(both)%2
yt = len(yt) - len(both)
yj = len(yj) - len(both)
if turn:
    if yj>yt: print('yj')
    else: print('yt')
else:
    if yt>yj: print('yt')
    else: print('yj')