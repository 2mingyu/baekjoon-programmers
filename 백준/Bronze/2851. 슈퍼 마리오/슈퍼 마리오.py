m = [int(input()) for _ in range(10)]
s = 0
for i in range(10):
    if abs(100-s) < abs(s+m[i]-100): break
    else: s += m[i]
print(s)