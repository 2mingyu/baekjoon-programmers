n = int(input())
c = list(map(float, input().split()))
s = 0
for e in c:
    s += e**3
print(s**(1/3))