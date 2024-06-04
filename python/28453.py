"""
Previous Level
"""
N = int(input())
M = list(map(int, input().split()))
for i in range(N):
    if M[i] == 300: M[i] = 1
    elif M[i] >= 275: M[i] = 2
    elif M[i] >= 250: M[i] = 3
    else: M[i] = 4
print(*M)