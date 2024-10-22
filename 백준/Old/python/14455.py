"""
Don't Be Last!
"""
d = {'Bessie': 0,
     'Elsie': 0,
     'Daisy': 0,
     'Gertie': 0,
     'Annabelle': 0,
     'Maggie': 0,
     'Henrietta': 0}
N = int(input())
for _ in range(N):
    a, b = input().split()
    d[a] += int(b)
s = set()
for i in d:
    s.add(d[i])
if len(s) > 1:
    t = sorted(s)[1]
    r = []
    for i in d:
        if d[i] == t:
            r.append(i)
    if len(r) == 1: print(r[0])
    else: print("Tie")
else: print("Tie")