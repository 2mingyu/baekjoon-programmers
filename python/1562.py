"""
계단 수

dp
경로 기록
비트마스킹 ..

dp[x][y][z] : x번째 자리수, 현재 숫자 y, visitied 횟수 z (1024개 종류)

visited는 0~9 방문을 이진수로 바꿔서..(비트마스킹)
아무것도 방문 안했으면 0 -> 0
0 방문했으면 1 -> 1
1 방문했으면 10 -> 2
1 0 방문했으면 11 -> 3
전부 방문했으면 111111111 -> 2023

| 연산 이용 : 각 비트 자리에 대해 or 연산
ex) 5|3 -> 7    (110 or 011 -> 111)
방문했던 곳 또 방문할 수 있으니 필요
"""
N = int(input())
dp = [[[0]*1024 for _ in range(10)] for _ in range(N)]
for j in range(1, 10):
    dp[0][j][2**j] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1024):
            if j-1 >= 0:
                dp[i][j][k|2**j] += dp[i-1][j-1][k]
            if j+1 <= 9:
                dp[i][j][k|2**j] += dp[i-1][j+1][k]
            dp[i][j][k|2**j] %= 1000000000

r = 0
for j in range(10):
    r += dp[-1][j][1023]
    r %= 1000000000

print(r)