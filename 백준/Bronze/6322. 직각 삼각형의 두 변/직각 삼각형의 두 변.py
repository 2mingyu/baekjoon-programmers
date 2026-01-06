i = 1
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break
    print(f'Triangle #{i}')
    if a == -1:
        a = c**2-b**2
        if a > 0:
            a = a**0.5
            print(f'a = {a:.3f}')
        else:
            print('Impossible.')
    elif b == -1:
        b = c**2-a**2
        if b > 0:
            b = b**0.5
            print(f'b = {b:.3f}')
        else:
            print('Impossible.')
    if c == -1:
        c = a**2+b**2
        if c > 0:
            c = c**0.5
            print(f'c = {c:.3f}')
        else:
            print('Impossible.')
    i += 1
    print()