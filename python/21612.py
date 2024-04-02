"""
Boiling Water
"""
B = int(input())
P = 5 * B - 400
print(P)
a = 100 - P
print(a//abs(a) if a else a)