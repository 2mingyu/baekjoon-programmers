"""
가장 긴 바이토닉 부분 수열
11053 : 가장 긴 증가하는 부분 수열
"""
N = int(input())
A = list(map(int, input().split()))
dp_increase = [1] * N
dp_decrease = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
        if A[N-j-1] < A[N-i-1]:
            dp_decrease[N-i-1] = max(dp_decrease[N-i-1], dp_decrease[N-j-1]+1)
result = 0
for i in range(N):
    result = max(result, dp_increase[i]+dp_decrease[i]-1)
print(result)