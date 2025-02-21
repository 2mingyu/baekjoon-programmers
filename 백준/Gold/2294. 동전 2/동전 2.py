n, k = map(int, input().split())
l = sorted(set([int(input()) for _ in range(n)]))
dp = [0] + [float('inf')]*k
for e in l:
    for i in range(e, k+1):
        dp[i] = min(dp[i], dp[i-e]+1)
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])
