for _ in range(3):
    s = input()
    a = 1
    c = 1
    for i in range(1, 8):
        if s[i] == s[i-1]:
            c += 1
            if c > a:
                a = c
        else:
            c = 1
    print(a)