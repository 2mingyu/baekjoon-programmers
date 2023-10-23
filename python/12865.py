"""
평범한 배낭
"""
N, K = map(int, input().split())
WV = []
dp = [0] * (K+1)
for _ in range(N): WV.append(list(map(int, input().split())))
for wv in WV:
    w = wv[0]
    v = wv[1]
    for i in range(K, w-1, -1): dp[i] = max(dp[i], v+dp[i-w])
print(dp[K])