import sys
input = sys.stdin.readline

n = int(input())
c = sorted([int(input()) for _ in range(n)], reverse=True)
H = 0
for e in c:
    if e >= H+1: H += 1
    else: break
print(H)