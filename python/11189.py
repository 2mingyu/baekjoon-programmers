"""
Toilet Seat
"""
s = input()
a = b = c = 0
d = e = f = s[0]
for i in range(1, len(s)):
    if s[i] != d: a += 1
    if s[i] != e: b += 1
    if s[i] != f: c += 1
    if s[i] == 'U': b += 1
    if s[i] == 'D': a += 1
    d = 'U'
    e = 'D'
    f = s[i]

print(a)
print(b)
print(c)