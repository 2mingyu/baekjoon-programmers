import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [0] * (n + 1)
for _ in range(m):
    k, s, e = map(int, input().split())
    if s >= l[k]:
        l[k] = e
        print("YES")
    else:
        print("NO")