w, h = map(int, input().split())
s = w*h
a = s//4840 + bool(s%4840)
print(a//5 + bool(a%5))