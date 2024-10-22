"""
메시지
"""
g = 1
while True:
    n = int(input())
    if n == 0: break
    p = []
    l = []
    for i in range(n):
        a = input().split()
        p. append(a[0])
        for j in range(1, n):
            if a[j] == 'N':
                l.append([i, (i-j) % (n)])
    print('Group', g)
    if l:
        for ll in l:
            print(p[ll[1]], 'was nasty about', p[ll[0]])
    else:
        print('Nobody was nasty')
    g += 1
    print()