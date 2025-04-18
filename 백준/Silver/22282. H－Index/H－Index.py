import sys
input = sys.stdin.readline

n = int(input())
c = sorted([int(input()) for _ in range(n)])
H = 0
while c and c.pop() >= H+1: H += 1
print(H)