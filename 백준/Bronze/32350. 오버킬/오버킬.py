N, D, p = map(int, input().split())
A = list(map(int, input().split()))
t = 0
i = 0
while i < N:
    if A[i] > 0:
        A[i] -= D
        if A[i] <= 0:
            if i+1 < N:
                A[i+1] -= -A[i]*p//100
            i += 1
        t += 1
    else:
        i += 1
print(t)