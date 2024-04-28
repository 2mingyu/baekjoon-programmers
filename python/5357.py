"""
Dedupe
"""
for _ in range(int(input())):
    s = input()
    t = ''
    r = ''
    for c in s:
        if c != t:
            r += c
        t = c
    print(r)