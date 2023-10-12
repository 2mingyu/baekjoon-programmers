"""
블랙잭
"""
N, M = map(int, input().split())
n = list(map(int, input().split()))
r = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if n[i]+n[j]+n[k] <= M: r = max(r, n[i]+n[j]+n[k])
print(r)