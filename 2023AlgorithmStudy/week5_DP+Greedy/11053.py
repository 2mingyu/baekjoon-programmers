"""
A = {10, 20, 10, 30, 20, 50}
dp = {1, 1, 1, 1, 1, 1}
check 20
    check 10.. 10 < 20
    dp = {1, 2, 1, 1, 1, 1}
check 10
    check 10 .. 10 == 10
    dp = {1, 2, 1, 1, 1, 1}
    check 20.. 10 > 20
    dp = {1, 2, 1, 1, 1, 1}
check 30
    check 10.. 10 < 30
    dp = {1, 2, 1, 2, 1, 1}
    check 20.. 20 < 30
    dp = {1, 2, 1, 3, 1, 1} // 20 위치의 dp인 2에 1을 더함
    check 10.. 10 < 30
    dp = {1, 2, 1, 3, 1, 1} // 10 위치의 dp인 1에 1을 더한 2 보다, 현재 30 위치의 dp인 3이 큼
"""
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))