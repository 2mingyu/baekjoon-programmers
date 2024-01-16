"""
LCS 2

dp[i][j]는 A[0:i+1]과 B[0:j+1] 까지 LCS 길이

A B 길이 다른 경우 생각해서, dp[-1][-1]이 아닌 dp[len(A)-1][len(B)-1] 이용
"""
A = " " + input()
B = " " + input()
l = max(len(A), len(B))
dp = [[0]*l for _ in range(l)]
i = j = 0
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(A)-1][len(B)-1])

if dp[len(A)-1][len(B)-1]:
    LCS = ""
    i = len(A)-1
    j = len(B)-1
    while dp[i][j] != 0:
        if A[i] == B[j]:
            LCS += A[i]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] == dp[i][j]:
                i -= 1
            else:
                j -= 1
    print(LCS[::-1])