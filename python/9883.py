"""
Morton Numbers
"""
x, y = map(int, input().split())
x2, y2 = bin(x)[2:], bin(y)[2:]
m = max(len(x2), len(y2))
x2, y2 = x2.zfill(m), y2.zfill(m)
z = ''
for i in range(m): z += x2[i] + y2[i]
print(int(z, 2))