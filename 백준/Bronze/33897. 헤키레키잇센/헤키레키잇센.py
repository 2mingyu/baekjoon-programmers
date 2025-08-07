N = int(input())
l = list(map(int, input().split()))
c = 1
r = m = 1
for i in range(1, N):
    if l[i] < l[i-1]:
        c += 1
        m = 1
    else:
        m += 1
    r = max(m, r)
print(c, r)