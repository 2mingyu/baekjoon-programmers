"""
ZOAC 6
"""
r = 0
for _ in range(int(input())):
    S = input()
    r += '01' in S or 'OI' in S
print(r)