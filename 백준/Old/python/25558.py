"""
내비게이션
"""
N = int(input())
sx, sy, ex, ey = map(int, input().split())
r = [0] * N
for i in range(N):
    x, y = sx, sy
    M = int(input())
    for j in range(M):
        xij, yij = map(int, input().split())
        r[i] += abs(x-xij) + abs(y-yij)
        x, y = xij, yij
    r[i] += abs(ex-x) + abs(ey-y)
print(r.index(min(r))+1)