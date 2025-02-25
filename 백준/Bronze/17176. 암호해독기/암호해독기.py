N = int(input())
l = sorted(list(map(int, input().split())))
s = ''.join(sorted(input()))
c = ''
for i in l:
    if i > 26: c += chr(i - 27 + 97)
    elif i: c += chr(i - 1 + 65)
    else: c += ' '
print('ny'[s==c])