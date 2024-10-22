"""
재수강
"""
S = input()
print(sum([input()[:5] == S[:5] for _ in range(int(input()))]))