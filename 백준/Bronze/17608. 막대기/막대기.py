import sys
input = sys.stdin.readline
N = int(input())
s = []
for _ in range(N):
    h = int(input())
    while s and s[-1] <= h:
        s.pop()
    s.append(h)
print(len(s))