N = int(input())
P = list(map(int, input().split()))
r = 0
s = P[0]
for i in range(1, N):
    if P[i] <= P[i-1]:
        r = max(r, P[i-1]-s)
        s = P[i]
r = max(r, P[-1]-s)
print(r)