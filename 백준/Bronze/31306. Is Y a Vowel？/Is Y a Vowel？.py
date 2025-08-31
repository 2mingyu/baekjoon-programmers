s = input()
a = sum([s.count(e) for e in 'aeiou'])
print(a, a+s.count('y'))