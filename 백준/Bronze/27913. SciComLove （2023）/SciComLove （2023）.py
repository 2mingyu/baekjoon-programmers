import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
s = ([1, 0, 0, 1, 0, 0, 1, 0, 0, 0] * ((N//10)+1))[:N]
c = sum(s)
for _ in range(Q):
    X = int(input())-1
    if s[X]:
        s[X] = 0
        c -= 1
    else:
        s[X] = 1
        c += 1
    print(c)