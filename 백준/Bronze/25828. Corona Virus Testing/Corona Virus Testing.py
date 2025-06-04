g, p, t = map(int, input().split())
a, b = g*p, g + t*p
if a < b: print(1)
elif a > b: print(2)
else: print(0)