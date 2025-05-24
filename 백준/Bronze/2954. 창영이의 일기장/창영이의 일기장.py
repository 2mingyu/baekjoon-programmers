a = input()
b = ''
i = 0
while i < len(a):
    b += a[i]
    if a[i] in 'aeiou' and i+1 < len(a) and a[i+1] == 'p' and i+2 < len(a) and a[i+2] == a[i]:
        i += 2
    i += 1
print(b)