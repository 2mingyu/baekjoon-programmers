"""
다이얼
"""
t = 0
for c in input():
    if c < 'D': t += 3
    elif c < 'G': t += 4
    elif c < 'J': t += 5
    elif c < 'M': t += 6
    elif c < 'P': t += 7
    elif c < 'T': t += 8
    elif c < 'W': t += 9
    else: t += 10
print(t)