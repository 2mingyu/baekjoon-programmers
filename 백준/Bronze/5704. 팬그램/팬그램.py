while True:
    s = input()
    if s == '*': break
    a = set()
    for e in s:
        if e != ' ':
            a.add(e)
    print('NY'[len(a)==26])