n, a, b = map(int, input().split())
F = 0
B = 0
FB = 0
for i in range(1, n+1):
    if i%a and i%b: continue
    elif i%a: B += 1
    elif i%b: F += 1
    else: FB += 1
print(F, B, FB)