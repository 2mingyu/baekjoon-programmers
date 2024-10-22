"""
카드 공장 (Small)
"""
N, M = map(int, input().split())
c = []
for _ in range(N):
    A, B = map(int, input().split())
    c.append([A, B])
for _ in range(M):
    K = int(input())
    for i in range(N):
        if c[i][0] <= K:
            t = c[i][0]
            c[i][0] = c[i][1]
            c[i][1] = t
s = 0
for i in range(N):
    s += c[i][0]
print(s)