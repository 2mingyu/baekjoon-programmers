"""
DFS와 BFS
"""
def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')
    for i in range(1, len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in range(1, len(graph)):
            if graph[start][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (N+1)
dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(graph, V, visited)