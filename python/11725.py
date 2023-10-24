"""
트리의 부모 찾기
"""
from collections import deque
N = int(input())
link = {i: set() for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    link[a].add(b)
    link[b].add(a)
visited = {1}
parents = [0 for _ in range(N+1)]
q = deque([1])
while q:
    node = q.popleft()
    for l in link[node]:
        if l not in visited:
            parents[l] = node
            visited.add(l)
            q.append(l)
for i in range(2, N+1):
    print(parents[i])