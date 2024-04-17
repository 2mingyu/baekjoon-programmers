"""
Zero or One
"""
A, B, C = map(int, input().split())
S = A+B+C
if S == 3 or S == 0: print('*')
elif S == 2:
    if not A: print('A')
    if not B: print('B')
    if not C: print('C')
else:
    if A: print('A')
    if B: print('B')
    if C: print('C')