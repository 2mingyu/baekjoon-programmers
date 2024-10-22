"""
Larger Sport Facility
"""
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    e = a*b - c*d
    if e > 0: print('TelecomParisTech')
    elif e == 0: print('Tie')
    else: print('Eurecom')