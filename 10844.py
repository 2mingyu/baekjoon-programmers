"""
쉬운 계단 수

앞자리부터 뒷자리로 가면서, 각각의 자리수에서 각 숫자의 경우 수
dp[N][10]
         0 1 2 3 4 5 6 7 8 9
dp[0] = [0,1,1,1,1,1,1,1,1,1]
dp[1] = [1,1,2,2,2,2,2,2,2,1]
답은 sum(dp[N-1])
dp[n][m] = dp[n-1][m-1] + dp[n-1][m+1]
"""
N = int(input())
dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(N-1):
    tmp = [dp[-1][1]]
    for j in range(1, 9): tmp.append(dp[-1][j-1] + dp[-1][j+1])
    tmp.append(dp[-1][8])
    dp.append(tmp)
print(sum(dp[-1]) % 1000000000)