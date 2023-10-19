"""
보물
출력은 S이기 때문에 B를 정렬해도 상관 없음
"""
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
S = 0
for i in range(N): S += A[i]*B[i]
print(S)