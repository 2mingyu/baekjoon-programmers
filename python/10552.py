"""
DOM

싫어하는 채널에서 좋아하는 채널로 방향 그래프가 그려지는 느낌
"""
N, M, P = map(int, input().split())
g = dict()
for i in range(N):
    a, b = map(int, input().split())
    if b not in g:
        g[b] = a
visited = [0]*(M+1)
r = 0
while True:
    if P not in g:
        print(r)
        exit()
    P = g[P]
    if visited[P]:
        print(-1)
        exit()
    visited[P] = 1
    r += 1