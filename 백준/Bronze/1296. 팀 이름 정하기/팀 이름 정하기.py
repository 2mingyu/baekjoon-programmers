S = input()
N = int(input())
c = 0
r = ''
for _ in range(N):
    i = input()
    t = S + i
    L, O, V, E = t.count('L'), t.count('O'), t.count('V'), t.count('E')
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if p > c:
        c = p
        r = i
    elif p == c:
        if i < r:
            r = i
    if not r: r = i
print(r)