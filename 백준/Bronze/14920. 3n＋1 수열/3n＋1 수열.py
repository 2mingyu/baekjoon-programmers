n = 1
C = int(input())
while C != 1:
    n += 1
    if C%2: C = 3*C + 1
    else: C = C//2
print(n)