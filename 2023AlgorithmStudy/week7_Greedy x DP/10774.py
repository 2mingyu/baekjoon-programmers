"""
저지
"""
import sys
J = int(input())
A = int(input())
size = [0]
result = 0
for _ in range(J):
    tmp = sys.stdin.readline().strip()
    if tmp == 'L': size.append(3)
    elif tmp == 'M': size.append(2)
    elif tmp == 'S': size.append(1)
for _ in range(A):
    s, n = sys.stdin.readline().strip().split()
    n = int(n)
    if size[n]:
        if s == 'L':
            if size[n] >= 3:
                result += 1
                size[n] = 0
        elif s == 'M':
            if size[n] >= 2:
                result += 1
                size[n] = 0
        elif s == 'S':
            if size[n] >= 1:
                result += 1
                size[n] = 0
print(result)