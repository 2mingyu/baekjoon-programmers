"""
하얀 칸
"""
r = 0
for i in range(8):
    s = input()
    for j in range(8):
        if (i+j) % 2 == 0 and s[j] == 'F':
            r += 1
print(r)