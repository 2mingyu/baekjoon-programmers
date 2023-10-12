"""
Four Squares
1 = 1
2 = 1 1
3 = 1 1 1
4 = 4
5 = 4 1
6 = 4 1 1
7 = 4 1 1 1
8 = 4 4
9 = 9
10 = 9 1
11 = 9 1 1
12 = 9 1 1 1 or 4 4 4 4
PyPy3로 해야 시간 초과 안나옴
"""
n = int(input())
dp = [0] + [5]*n
dp[1] = 1
for i in range(2, n+1):
    j = 1
    while i - j*j >= 0:
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1
print(dp[n])