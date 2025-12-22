r = input()
s = r.split('|')
x = ''
for e in s:
    x += e[0]
c = x.count('C') + x.count('F') + x.count('G')
e = x.count('E') + x.count('A') + x.count('D')
if c > e or (c == e and r[-1] in 'CFG'): print('C-major')
else: print('A-minor')