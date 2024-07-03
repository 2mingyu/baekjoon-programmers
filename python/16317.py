"""
Code Cleanups
"""
n = int(input())
d = list(map(int, input().split()))
i = 0
j = 0
s = 0
r = 0
for k in range(1, 366):
    if i < len(d):
        if d[i] == k:
            j += 1
            i += 1
    if s + j >= 20:
        j = 0
        s = 0
        r += 1
    else: s += j
if j: r += 1
print(r)