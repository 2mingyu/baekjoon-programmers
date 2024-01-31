"""
모음의 개수
"""
s = input()
print(sum(s.count(c) for c in 'aeiou'))