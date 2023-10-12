"""
포도주 시식

dp[n] = l[n] + max(dp[n-2], l[n-1]+dp[n-3])
다이나믹 프로그래밍인거 바로 알아차렸지 만
l[n-1]을 dp[n-1]로 생각해서 고치느라 오래 걸림
dp[3] 도 틀렸었고
마시지 않고 넘어가는 걸 생각 못해서 아주 많이 틀림
"""
l = []
n = int(input())
dp = [0] * n
for i in range(n):
    l.append(int(input()))
dp[0] = l[0]
if n > 1:
    dp[1] = l[0]+l[1]

if n > 2:
    dp[2] = max(l[2]+l[1], l[2]+l[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+l[i-1]+l[i], dp[i-2]+l[i])
print(dp[n-1])