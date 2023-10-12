"""
집합
"""
import sys
S = set()
for _ in range(int(input())):
    c = sys.stdin.readline().split()
    if c[0] == 'add':
        if int(c[1]) not in S:
            S.add(int(c[1]))
    elif c[0] == 'remove':
        if int(c[1]) in S:
            S.remove(int(c[1]))
    elif c[0] == 'check':
        print(int(int(c[1]) in S))
    elif c[0] == 'toggle':
        if int(c[1]) in S:
            S.remove(int(c[1]))
        else:
            S.add(int(c[1]))
    elif c[0] == 'all':
        S = set(range(1,21))
    elif c[0] == 'empty':
        S = set()