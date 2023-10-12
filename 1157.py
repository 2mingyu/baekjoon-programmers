"""
단어 공부
print(ord('a'), ord('z'), ord('A'), ord('Z'))
97 122 65 90
"""
W = input()
a = [0] * 26
for w in W:
    if ord(w) >= 97: a[ord(w)-97] += 1
    else: a[ord(w)-65] += 1
maxAlphabet = -1
maxCount = max(a)
for aa in range(26):
    if a[aa] == maxCount:
        if maxAlphabet == -1: maxAlphabet = aa
        else:
            print("?")
            exit(0)
print(chr(maxAlphabet+65))