import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

g = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in range(1, N + 1):
    g[i].sort()

visited = [0] * (N + 1)
q = deque([R])
visited[R] = 1
cnt = 1

while q:
    u = q.popleft()
    for v in g[u]:
        if not visited[v]:
            cnt += 1
            visited[v] = cnt
            q.append(v)

for i in range(1, N + 1):
    print(visited[i])