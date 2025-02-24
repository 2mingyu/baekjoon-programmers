N = int(input())
A = input().split()

b = A[0]
t = 1
l = []
for i in range(1, N):
    if A[i] == b:
        t += 1
    else:
        l.append(t)
        b = A[i]
        t = 1
l.append(t)

ans = max(l)
for i in range(len(l) - 1):
    ans = max(ans, l[i] + l[i+1])
print(ans)
