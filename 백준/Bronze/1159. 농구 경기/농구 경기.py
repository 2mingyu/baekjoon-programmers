d = [0]*26
for _ in range(int(input())):
    d[ord(input()[0]) - ord('a')] += 1
s = ''
for i in range(26):
    if d[i] >= 5:
        s += chr(i+97)
print(s if s else 'PREDAJA')