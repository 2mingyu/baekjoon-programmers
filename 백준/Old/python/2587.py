"""
대표값2
"""
l = []
for _ in range(5): l.append(int(input()))
l.sort()
print(sum(l)//5)
print(l[2])