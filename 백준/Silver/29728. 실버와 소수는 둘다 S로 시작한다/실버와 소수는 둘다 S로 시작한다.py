N = int(input())
p = [False, False] + [True] * (N-1)

A = ''
B = 0
S = 0
for i in range(1, N+1):
    if p[i]:
        for j in range(i * 2, N + 1, i):
            p[j] = False
    if p[i]:
        if A == 'B':
            B -= 1
            S += 1
        S += 1
        A = 'S'
    else:
        B += 1
        A = 'B'
print(B, S)