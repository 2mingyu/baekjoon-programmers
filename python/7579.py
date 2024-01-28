"""
앱

dp[i][j]: i번째 앱까지 j만큼 비용을 사용했을 때 얻을 수 있는 최대 메모리
"""
N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))

s = sum(c)
dp = [[0]*(s+1) for _ in range(N)]
r = s

for i in range(N):
    for j in range(s):
        if j < c[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-c[i]] + m[i], dp[i-1][j])
        if dp[i][j] >= M:
            r = min(r, j)

print(r)