"""
스택
"""
import sys
s = []
for _ in range(int(input())):
    c = sys.stdin.readline().split()
    if c[0] == 'push': s.append(c[1])
    elif c[0] == 'pop':
        if s: print(s.pop())
        else: print(-1)
    elif c[0] == 'size': print(len(s))
    elif c[0] == 'empty':
        if s: print(0)
        else: print(1)
    elif c[0] == 'top':
        if s: print(s[-1])
        else: print(-1)