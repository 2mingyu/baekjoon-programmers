"""
Cowspeak
"""
for _ in range(int(input())):print("".join(chr(c.count('M')*16+c.count('O')) for c in input().split()))
