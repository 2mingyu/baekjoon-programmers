a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
while a2 > 0 and b2 > 0:
    a2 -= b1
    b2 -= a1
if a2 > 0: print('PLAYER A')
elif b2 > 0: print('PLAYER B')
else: print('DRAW')