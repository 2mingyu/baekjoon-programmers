N = int(input())
l = input().split()
d = {}
r = float('inf')
for i in range(N):
    if l[i] in d:
        d[l[i]].append(i)
    else:
        d[l[i]] = [i]
for e in d:
    if len(d[e]) > 4:
        for i in range(len(d[e]) - 4):
            r = min(r, d[e][i+4] - d[e][i] + 1)

if r == float('inf'): print(-1)
else: print(r)