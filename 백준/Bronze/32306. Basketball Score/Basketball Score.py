a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
s1 = a + 2*b + 3*c
s2 = d + 2*e + 3*f
print(1 if s1 > s2 else 2 if s2 > s1 else 0)