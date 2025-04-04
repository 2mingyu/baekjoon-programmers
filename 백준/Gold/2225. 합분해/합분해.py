N, K = map(int, input().split())
dp = [0] + [1]*K
for n in range(N):
    for k in range(1, K+1):
        dp[k] = (dp[k] + dp[k-1]) % 10**9
print(dp[K])