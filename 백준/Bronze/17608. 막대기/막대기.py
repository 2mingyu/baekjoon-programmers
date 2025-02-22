import sys
input = sys.stdin.readline
N = int(input())
l = [int(input()) for _ in range(N)]
m = 0
r = 0
for e in l[::-1]:
    if m < e:
        m = e
        r += 1
print(r)