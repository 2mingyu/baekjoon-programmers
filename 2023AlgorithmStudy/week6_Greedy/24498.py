"""
blobnom
((인접한 두 탑의 min)+자신)이 max가 되는 탑을 선택
양 끝이 최대 높이일 수도 있으므로 처음에 result = max(A[0], A[N-1]) 넣기
"""
N = int(input())
A = list(map(int, input().split()))
result = max(A[0], A[N-1])
for i in range(1, N-1):
    result = max(result, A[i] + min(A[i-1], A[i+1]))
print(result)