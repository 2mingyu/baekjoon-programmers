r = 0
for c in input():
    if c in 'AabDdegOoPpQqR@': r += 1
    elif c == 'B': r += 2
print(r)