n = int(input())
gp = {'A':4, 'B':3, 'C':2, 'D':1, 'E':0}

a = 0
b = 0

for _ in range(n):
    g, t = input().strip()
    t = int(t)

    a += gp[g]

    if g in "ABC":
        if t == 1:
            b += 0.05
        elif t == 2:
            b += 0.025

gpa = a / n + b
print(gpa)