"""
Hashing
"""
L = int(input())
s = [ord(c)-96 for c in input()]
r = 0
for i in range(L): r += s[i] * (31**i)
print(r%1234567891)