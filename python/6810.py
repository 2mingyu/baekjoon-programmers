"""
ISBN
"""
s = '9780921418' + input() + input() + input()
print('The 1-3-sum is', sum([int(a) for a in s[::2]]) + sum([int(a) for a in s[1::2]]) * 3)