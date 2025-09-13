while True:
    N = input()
    if N == '0': break
    r = 0
    for e in N:
        if int(e) == 0: r += 5
        elif int(e) == 1: r += 3
        else: r += 4
    print(r+1)