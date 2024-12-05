l = [''] * 10000
for i in range(5):
    s = input()
    for j in range(len(s)):
        l[j] += s[j]
for j in range(10000):
    if l[j] == '.omln':
        l[j] = 'owln.'
    elif l[j] == 'owln.':
        l[j] = '.omln'
for i in range(5):
    for j in range(10000):
        if len(l[j]) == 5:
            print(l[j][i], end='')
    print()