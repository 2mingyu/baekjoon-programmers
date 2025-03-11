MOD = 1000007

w, h = map(int, input().split())
x, y = map(int, input().split())

dp1 = [[0]*(x+1) for _ in range(y+1)]
dp1[1][1] = 1
for i in range(1, y+1):
    for j in range(1, x+1):
        dp1[i][j] = (dp1[i-1][j] + dp1[i][j-1] + dp1[i][j]) % MOD

dp2 = [[0]*(w-x+2) for _ in range(h-y+2)]
dp2[1][1] = 1
for i in range(1, h-y+2):
    for j in range(1, w-x+2):
        dp2[i][j] = (dp2[i-1][j] + dp2[i][j-1] + dp2[i][j]) % MOD

print((dp1[-1][-1] * dp2[-1][-1]) % MOD)