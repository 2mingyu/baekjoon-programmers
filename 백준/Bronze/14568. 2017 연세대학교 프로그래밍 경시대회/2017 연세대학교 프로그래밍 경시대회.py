N = int(input())
r = 0
for A in range(1, N+1):
    for B in range(1, N+1):
        for C in range(1, N+1):
            if A+B+C == N and C >= B+2 and A%2 == 0:
                r += 1
print(r)