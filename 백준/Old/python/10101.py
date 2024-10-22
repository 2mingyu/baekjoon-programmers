"""
삼각형 외우기
"""
t = [int(input()) for _ in range(3)]
if sum(t) != 180: print('Error')
elif t[0] == t[1] == t[2]: print('Equilateral')
elif t[0] == t[1] or t[1] == t[2] or t[0] == t[2]: print('Isosceles')
else: print('Scalene')