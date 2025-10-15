d = set()
N = int(input())
for e in input().split(): d.add(e)
M = int(input())
for e in input().split(): d.add(e)
K = int(input())
for e in input().split():
    if e in d:
        d.remove(e)
S = int(input())
s = list(input())
for i in range(S):
    if s[i] in d:
        s[i] = ' '
s = ''.join(s)
s = s.split()
for e in s: print(e)