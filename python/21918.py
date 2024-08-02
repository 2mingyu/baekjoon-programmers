"""
전구
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(M):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        A[b] = c
    elif a == 2:
        for i in range(b, c):
            A[i] = not A[i]
    elif a == 3:
        for i in range(b, c):
            A[i] = 0
    elif a == 4:
        for i in range(b, c):
            A[i] = 1

print(' '.join(map(str, map(int, A))))