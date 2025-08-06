T = int(input())
for x in range(1, T+1):
    y = ''
    N = int(input())
    l = sorted([input() for i in range(N)])
    m = 0
    for e in l:
        s = set(e)
        t = len(s) - (' ' in s)
        if t > m:
            y = e
            m = t
    print(f'Case #{x}: {y}')