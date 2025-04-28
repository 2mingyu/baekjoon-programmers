N = int(input())
Y = M = 0
for t in list(map(int, input().split())):
    Y += (t//30 + 1) * 10
    M += (t//60 + 1) * 15
if Y > M:
    print('M', M)
elif M > Y:
    print('Y', Y)
else:
    print('Y M', Y)