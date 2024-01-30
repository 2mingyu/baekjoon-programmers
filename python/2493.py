"""
탑
"""
N = int(input())
A = [100000001] + list(map(int, input().split()))
stack = []
B = [0] * (N+1)

for i in range(1, N+1):
    while stack and stack[-1][1] < A[i]:
        stack.pop()
    if stack:
        B[i] = stack[-1][0]
    stack.append((i, A[i]))

print(*B[1:])