"""
줄 세우기

위상 정렬 ..
degree = 진입차수
"""
from collections import deque
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    degree[b] += 1

q = deque()
r = []
for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    a = q.popleft()
    r.append(a)
    for i in edges[a]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

print(*r)