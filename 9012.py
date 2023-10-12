"""
괄호
"""
for _ in range(int(input())):
    s = 0
    for c in input():
        if c == '(': s += 1
        elif c == ')': s -= 1
        if s < 0: break
    if s == 0: print("YES")
    else: print("NO")