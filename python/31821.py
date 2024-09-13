"""
학식 사주기
"""
N = int(input())
A = []
for i in range(N): A.append(int(input()))
M = int(input())
r = 0
for j in range(M): r += A[int(input())-1]
print(r)
