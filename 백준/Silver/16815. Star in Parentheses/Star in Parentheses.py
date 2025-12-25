S = input()
s = []
for c in S:
    if c == '(':
        s.append('(')
    elif c == ')':
        if len(s)>0 and s[-1] == '(':
            s.pop()
        else:
            s.append(')')
    else:
        s.append('*')

F = False
a = b = 0
for e in s:
    if e == '(':
        if not F:
            a += 1
    elif e == '*':
        F = True
    else:
        if F:
            b += 1
print(min(a, b))
