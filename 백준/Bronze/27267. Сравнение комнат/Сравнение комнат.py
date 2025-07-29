a, b, c, d = map(int, input().split())
m, p = a*b, c*d
if m > p: print('M')
elif m == p: print('E')
else: print('P')