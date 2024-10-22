"""
Speed fines are not fine!
"""
a = int(input())
b = int(input())
c = b - a
d = 0
if c <= 0: d = 0
elif c <= 20: d = 100
elif c <= 30: d= 270
else: d = 500
if d: print('You are speeding and your fine is $'+str(d)+'.')
else: print('Congratulations, you are within the speed limit!')