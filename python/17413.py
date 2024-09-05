"""
단어 뒤집기 2
"""
S = input()
r = []
stack = []
tag = False
for c in S:
    if c == '<':
        tag = True
        while stack:
            r.append(stack.pop())
        r.append(c)
    elif c == '>':
        tag = False
        r.append(c)
    elif c == ' ':
        if tag:
            r.append(c)
        else:
            while stack:
                r.append(stack.pop())
            r.append(c)
    else:
        if tag:
            r.append(c)
        else:
            stack.append(c)

while stack:
    r.append(stack.pop())

for c in r:
    print(c, end='')