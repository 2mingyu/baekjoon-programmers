T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())
    t = d+n*p-n*s
    if t > 0: print('do not parallelize')
    elif t == 0: print('does not matter')
    else: print('parallelize')