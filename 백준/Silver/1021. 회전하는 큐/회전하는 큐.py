N, M = map(int, input().split())
l = list(map(int, input().split()))
i = 0
r = 0
while i < M:
    a = l[i]-1
    b = N+1-l[i]
    i += 1
    if a < b:
        r += a
        for j in range(i, M):
            l[j] = l[j]-a-1
            if l[j] < 1: l[j] += N
    else:
        r += b
        for j in range(i, M):
            l[j] = l[j]+b-1
            if l[j] > N: l[j] -= N
    N -= 1
print(r)