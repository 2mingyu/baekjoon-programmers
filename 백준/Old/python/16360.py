"""
Go Latin
"""
d = {
    'a': 'as',
    'i': 'ios',
    'y': 'ios',
    'l': 'les',
    'n': 'anes',
    'o': 'os',
    'r': 'res',
    't': 'tas',
    'u': 'us',
    'v': 'ves',
    'w': 'was'
}
for _ in range(int(input())):
    s = input()
    if s[-1] in d:
        print(s[:-1]+d[s[-1]])
    elif s[-2:] == 'ne':
        print(s[:-2]+'anes')
    else:
        print(s+'us')