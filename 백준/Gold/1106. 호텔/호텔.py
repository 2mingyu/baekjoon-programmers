C, N = map(int, input().split())
dp = [float('inf')] * (C+101)
dp[0] = 0
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(B, len(dp)):
        dp[i] = min(dp[i-B]+A, dp[i])
print(min(dp[C:]))