"""
삼각형과 세 변
"""
while True:
    l = sorted(list(map(int, input().split())))
    if l[0] == l[1] == l[2]:
        if l[0] == 0: break
        else: print('Equilateral')
    elif l[0] + l[1] > l[2]:
        if l[0] == l[1] or l[1] == l[2]:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')