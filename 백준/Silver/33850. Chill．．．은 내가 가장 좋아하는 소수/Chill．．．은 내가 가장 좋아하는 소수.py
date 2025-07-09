p = [True]*200001
for i in range(2, 200001):
    j = i*2
    while j < 200001:
        p[j] = False
        j += i

n, a, b = map(int, input().split())
m = [[0] + list(map(int, input().split())) for _ in range(2)]
dp = [0]*(n+1)
dp[0] = 0
dp[1] = a if p[m[0][1]+m[1][1]] else b
for i in range(2, n+1):
    t1 = dp[i-2]
    t1 += a if p[m[0][i-1]+m[0][i]] else b
    t1 += a if p[m[1][i-1]+m[1][i]] else b
    t2 = dp[i-1]
    t2 += a if p[m[0][i]+m[1][i]] else b
    dp[i] = max(t1, t2)
print(dp[-1])