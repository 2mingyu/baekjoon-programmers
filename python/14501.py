"""
퇴사
4일의 최대보수 = 3일까지 최대보수 + 4일 일(될경우)
               2일까지 최대보수 + 3일 일
               1일까지 최대보수 + 2일 일
               0일까지 최대보수 + 1일 일
                                           중에서 max

4일 일이 되려면? T[4] = 1
3일 일이 되려면? T[3] <= 2
2일 일이 되려면? T[2] <= 3
1일 일이 되려면? T[1] <= 4
"""
N = int(input())
T, P, dp = [10000], [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    dp.append(0)

for i in range(1, N+1):
    for j in range(i):
        tmp = dp[j]
        if T[j+1] <= i-j:
            tmp += P[j+1]
        dp[i] = max(dp[i], tmp)

print(dp[N])