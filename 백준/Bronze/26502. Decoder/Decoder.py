d = {'y': 'a',
     'a': 'e',
     'e': 'i',
     'i': 'o',
     'o': 'u',
     'u': 'y',
     'Y': 'A',
     'A': 'E',
     'E': 'I',
     'I': 'O',
     'O': 'U',
     'U': 'Y'}
n = int(input())
for _ in range(n):
    s = input()
    for e in s:
        print(d[e] if e in d else e, end='')
    print()