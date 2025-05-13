while True:
    s = input()
    if s == '0': break
    r = ''
    t = s[0]
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            c += 1
        else:
            r += str(c)+t
            t = s[i]
            c = 1
    r += str(c)+t
    print(r)