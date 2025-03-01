import sys
input = sys.stdin.readline

s = []
N = int(input())
for _ in range(N):
    c = list(map(int, input().split()))
    if c[0] == 1: s.append(c[1])
    elif c[0] == 2:
        if s: print(s.pop())
        else: print(-1)
    elif c[0] == 3: print(len(s))
    elif c[0] == 4: print(int(bool(len(s) == 0)))
    else:
        if s: print(s[-1])
        else: print(-1)