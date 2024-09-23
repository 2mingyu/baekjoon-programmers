"""
30

맨 뒤가 0으로 끝나야 하므로, 0이 있어야 한다.
각 자리수의 합이 3의 배수면 3의 배수다.
"""
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