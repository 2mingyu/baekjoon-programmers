a = input()
b = a + '0000'

i = len(a) - 1
j = len(b) - 1
c = 0
r = []

while i >= 0 or j >= 0 or c:
    x = int(a[i]) if i >= 0 else 0
    y = int(b[j]) if j >= 0 else 0
    s = x + y + c
    r.append(str(s % 2))
    c = s // 2
    i -= 1
    j -= 1

print(''.join(r[::-1]))