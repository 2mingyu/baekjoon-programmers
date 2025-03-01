N = input()
if '0' not in N: print(-1)
else:
    t = 0
    for i in N:
        t += int(i)
    if t % 3:
        print(-1)
    else:
        print(''.join(sorted(list(N), reverse=True)))