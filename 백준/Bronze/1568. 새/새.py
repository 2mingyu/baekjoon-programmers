N = int(input())
K = 1
r = 0
while N:
    if N < K:
        K = 1
    N -= K
    K += 1
    r += 1
print(r)