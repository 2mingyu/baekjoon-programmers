"""
모비스
"""
s = set()
for n in input():
    if n in 'MOBIS': s.add(n)
print('YES' if len(s) == 5 else 'NO')