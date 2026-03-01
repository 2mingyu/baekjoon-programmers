import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    r = 0
    for a in range(1, n):
        for b in range(a+1, n):
            r += (a**2+b**2+m)%(a*b) == 0
    print(r)