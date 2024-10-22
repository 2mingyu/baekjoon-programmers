"""
Congruent Numbers
"""
p1, q1, p2, q2 = map(int, input().split())
r = p1*p2 / (q1*q2) / 2
print(int(int(r) == r))