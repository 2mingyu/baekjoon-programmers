n = int(input())
s = input().split()
r = []
for c in s:
    t = ''
    for i in range(0, len(c)-1, 2):
        t += chr(((ord(c[i])-97 + ord(c[i+1])-97 - n) % 26) + 97)
    r.append(t)
print(*r)