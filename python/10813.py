"""
공 바꾸기
"""
N, M = map(int, input().split())
b = [i for i in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    b[i], b[j] = b[j], b[i]
print(*b[1:])