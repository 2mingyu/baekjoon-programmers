import sys
input = sys.stdin.readline
f = [1, 2, 6, 24, 120]
while True:
    n = input().strip()[::-1]
    if n == '0': break
    s = 0
    for i in range(len(n)):
        s += int(n[i])*f[i]
    print(s)