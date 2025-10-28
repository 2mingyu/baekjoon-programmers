for _ in range(int(input())):
    s = input()
    l = len(s)
    print('Do-it' + ['-Not', ''][s[l//2-1] == s[l//2]])