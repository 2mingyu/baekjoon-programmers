"""
Every Second Counts
"""
h1, m1, s1 = map(int, input().split(' : '))
h2, m2, s2 = map(int, input().split(' : '))
x = h2*3600+m2*60+s2-h1*3600-m1*60-s1
if x < 0: print(x+86400)
else: print(x)