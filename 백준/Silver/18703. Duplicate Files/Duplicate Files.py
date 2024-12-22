import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    d = {}
    N = int(input())
    for _ in range(N):
        name, ID = input().split()
        if name in d:
            d[name] = min(d[name], int(ID))
        else:
            d[name] = int(ID)
    r = [d[e] for e in d]
    print(*sorted(r))
