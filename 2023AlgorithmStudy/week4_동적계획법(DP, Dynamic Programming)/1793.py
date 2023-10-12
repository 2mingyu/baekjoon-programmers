"""
11727번과 같음
1: 1 (세로)
2: 1+1+1 (세로세로)+(가로가로)+(2x2)
방법(n) = 방법(n-1) + 방법(n-2) * 2
(방법(n-1)에서 끝에 세로로 하나 추가) + (방법(n-2)에서 끝에 가로2개로 추가) + (방법(n-2)에서 끝에 2x2로 추가)
"""
a = [0 for i in range(251)] # a[n]은 2xn 크기의 직사각형을 채우는 방법의 수
while True:
    try:
        n = int(input())
        a[0] = 0
        a[1] = 1
        a[2] = 3
        for i in range(3, n + 1):
            a[i] = a[i-1] + a[i-2]*2
        print(a[n])
    except:
        break
# 위 코드는 틀렸다 그러고 아래 코드만 맞다고 그러네
dp = [0 for i in range(251)]
while(True):
    try:
        n = int(input())
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        for i in range(3,n+1):
            dp[i] = dp[i - 1] + 2 * dp[i - 2]
        print(dp[n])
    except:
        break
