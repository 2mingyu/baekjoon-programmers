import sys
input = sys.stdin.readline
n = int(input())
x = [int(input()) for _ in range(n)]
r = 0
for i in range(1, n):
    r += (x[i] - x[i-1])**2
print(r)