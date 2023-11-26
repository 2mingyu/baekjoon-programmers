"""
세로읽기
"""
s = []
for _ in range(5):
    s.append(input())
m = max([len(s[i]) for i in range(5)])
r = ""
for x in range(m):
    for y in range(5):
        if x < len(s[y]):
            r += s[y][x]
print(r)