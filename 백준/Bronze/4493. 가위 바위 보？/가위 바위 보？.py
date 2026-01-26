A = {'R S', 'S P', 'P R'}
t = int(input())
for _ in range(t):
    n = int(input())
    a = b = 0
    for _ in range(n):
        s = input()
        if s in A: a += 1
        elif s[::-1] in A: b += 1
    if b > a: print('Player 2')
    elif b < a: print('Player 1')
    else: print('TIE')