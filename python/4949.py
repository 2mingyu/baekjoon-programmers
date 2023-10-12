"""
균형잡힌 세상

스택
"""
while True:
    s = input()
    if s == '.': break
    l = []
    for c in s:
        if c == '(': l.append('(')
        elif c == '[': l.append('[')
        elif c == ')':
            if l and l[-1] == '(': l.pop()
            else:
                r = 'no'
                l.append(' ')
                break
        elif c == ']':
            if l and l[-1] == '[': l.pop()
            else:
                r = 'no'
                l.append(' ')
                break
    if l: r = 'no'
    else: r = 'yes'
    print(r)