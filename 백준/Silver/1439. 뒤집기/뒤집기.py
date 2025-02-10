S = input()
z = S.split('1')
o = S.split('0')
print(min(len(o) - o.count(''), len(z) - z.count('')))