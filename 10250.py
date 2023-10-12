"""
ACM 호텔
"""
for _ in range(int(input())):
    H, W, N = map(int, input().split())
    Y = N % H
    X = (N//H) + 1
    if Y == 0:
        Y = H
        X -= 1
    print(str(Y)+f'{X:02}')