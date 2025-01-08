n = int(input())
for _ in range(n):
    s = input()
    mack = False
    zack = False
    for c in s.split():
        if c == '18':
            mack = True
        elif c == '17':
            zack = True
    print(s)
    if mack and zack:
        print('both')
    elif mack:
        print('mack')
    elif zack:
        print('zack')
    else:
        print('none')
    print()