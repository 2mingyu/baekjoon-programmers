while True:
    l = sorted(list(map(int, input().split())))
    if sum(l):
        print(['wrong', 'right'][l[2]**2 == l[0]**2 + l[1]**2])
    else:
        break