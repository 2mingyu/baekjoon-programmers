"""
너의 티어는?

점수 분포가 1000~3000까지 50씩 뜀.
dp[i=0~20][j=0~40]
i = 게임횟수
1000 + 50 * j = 점수
dp[i][j] = 확률
"""
W, L, D = map(float, input().split())
dp = [[0 for j in range(41)] for i in range(21)]
dp[0][20] = 1
for i in range(1, 21):
    j = 0
    dp[i][0] = dp[i-1][j+1] * L + dp[i-1][j] * D
    for j in range(1, 40):
        dp[i][j] = dp[i-1][j-1] * W + dp[i-1][j+1] * L + dp[i-1][j] * D
    j = 40
    dp[i][40] = dp[i-1][j-1] * W + dp[i-1][j] * D
Bronze = 0
for j in range(0, 10): Bronze += dp[20][j]
Silver = 0
for j in range(10, 20): Silver += dp[20][j]
Gold = 0
for j in range(20, 30): Gold += dp[20][j]
Platinum = 0
for j in range(30, 40): Platinum += dp[20][j]
Diamond = dp[20][40]
print(format(round(Bronze, 8), '.8f'))
print(format(round(Silver, 8), '.8f'))
print(format(round(Gold, 8), '.8f'))
print(format(round(Platinum, 8), '.8f'))
print(format(round(Diamond, 8), '.8f'))