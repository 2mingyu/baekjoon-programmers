"""
IOIOI
"""
N = int(input())
M = int(input())
S = input()
l = []
i = 0
c = 0
while i < M:
    if S[i:i+3] == 'IOI':
        c += 1
        i += 2
    else:
        l.append(c)
        c = 0
        i += 1
r = 0
for ll in l:
    if ll + 1 - N > 0:
        r += ll + 1 - N
print(r)