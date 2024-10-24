N, H = map(int, input().split())
A = sorted(list(map(int, input().split())))
dp = [0] * (H+1)
for i in range(N):
    if A[i] <= H:
        dp[A[i]] += 1
for h in range(H+1):
    for i in range(N):
        if h-A[i] >= 0:
            dp[h] += dp[h-A[i]]
            dp[h] %= 1000000007
print(dp[H])