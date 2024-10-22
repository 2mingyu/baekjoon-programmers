"""
죽음의 게임
"""
N, K = map(int, input().split())
d = {i: int(input()) for i in range(N)}
v = [0] * N
M = 0
p = 0
v[p] = 1
while True:
    p = d[p]
    if v[p]:
        print(-1)
        exit()
    v[p] = 1
    M += 1
    if p == K:
        break
print(M)