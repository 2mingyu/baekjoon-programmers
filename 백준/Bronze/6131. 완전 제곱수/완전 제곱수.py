N = int(input())
c = 0
for B in range(1, 501):
    for A in range(B, 501):
        if B**2 + N == A**2:
            c += 1
print(c)