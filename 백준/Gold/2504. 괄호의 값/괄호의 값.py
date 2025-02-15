s = input()
l = []
for c in s:
    if c in '([':
        l.append(c)
    else:
        if not l:
            print(0)
            exit()
        t = 0
        p = l.pop()
        while l and str(p) not in '([':
            t += int(p)
            p = l.pop()
        if p == '(' and c == ')':
            if t:
                l.append(t*2)
            else:
                l.append(2)
        elif p == '[' and c == ']':
            if t:
                l.append(t*3)
            else:
                l.append(3)
        else:
            print(0)
            exit()

r = 0
for i in l:
    if str(i) in '([':
        print(0)
        exit()
    r += i
print(r)