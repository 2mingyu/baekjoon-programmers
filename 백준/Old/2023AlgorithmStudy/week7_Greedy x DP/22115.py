"""
창영이와 커피
DP같은데
1섭취
2섭취 = 2 or 1섭취 + 1
3섭취 = 3 or 2섭취 + 1 or 1섭취 + 2
https://cbkpar.tistory.com/56
참고..
"""
N, K = map(int, input().split())
C = list(map(int, input().split()))
dp = [100000] * (K + 1)
dp[0] = 0
for c in C:
    for i in range(K, c-1, -1):
        dp[i] = min(dp[i], dp[i-c]+1)
if dp[K] == 100000: print(-1)
else: print(dp[K])