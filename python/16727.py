"""
ICPC
"""
p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
f = p1 + p2 - s1 - s2
if f > 0: print('Persepolis')
elif f == 0:
    if p2 > s1: print('Persepolis')
    elif s1 > p2: print('Esteghlal')
    else: print('Penalty')
else: print('Esteghlal')