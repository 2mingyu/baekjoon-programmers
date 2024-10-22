"""
iSharp
"""
s = input().split()
i = 0
for x in s[1:]:
    n = ''
    i = 0
    while x[i] not in ['[', '&', '*', ',', ';']:
        n += x[i]
        i += 1
    y = ''
    while x[i] not in [',', ';']:
        if x[i] == '[':
            y = '[]' + y
            i += 2
        elif x[i] == '&':
            y = '&' + y
            i += 1
        elif x[i] == '*':
            y = '*'+ y
            i += 1
    print(s[0]+y, n+';')