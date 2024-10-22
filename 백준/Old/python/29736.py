"""
브실이와 친구가 되고 싶어 🤸‍♀️
"""
A, B = map(int, input().split())
K, X = map(int, input().split())
C, D = K-X, K+X
r = 0
for i in range(A, B+1):
    if C <= i <= D: r += 1
print(r if r else "IMPOSSIBLE")