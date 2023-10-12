"""
맥주 마시면서 걸어가기
"""
from collections import deque

def bfs():
    visited = set()
    queue = deque()
    visited.add(0)
    queue.append(0)
    while queue:
        now = queue.popleft()
        for neighbor in graph[now]:
            if neighbor == n+1: return 'happy'
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())
    node = []
    graph = []
    for _ in range(n+2):
        node.append(list(map(int, input().split())))
        graph.append([])
    for i in range(n+2):
        for j in range(i+1, n+2):
            if abs(node[j][0] - node[i][0]) + abs(node[j][1] - node[i][1]) <= 1000:
                graph[i].append(j)
                graph[j].append(i)
    print(bfs())