"""
가장 많은 글자
"""
import sys
a = 'abcdefghijklmnopqrstuvwxyz'
d = {x: 0 for x in a}
s = sys.stdin.read().replace('\n', '').replace(' ', '')
for c in s: d[c] += 1
m = max([d[x] for x in a])
for x in d:
    if d[x] == m: print(x, end="")