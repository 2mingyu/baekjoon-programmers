"""
Tabliczka
"""
a, b = map(int, input().split())
print(min(a, b) if a%2 & b%2 else 0)