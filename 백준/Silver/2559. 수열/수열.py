N, K = map(int, input().split())
t = list(map(int, input().split()))
r = s = sum(t[:K])
for i in range(K, N):
    s = s + t[i] - t[i-K]
    r = max(r, s)
print(r)