"""
파티
X에서 각각 노드로 최단거리는 X를 출발지로 한 다익스트라
각각 노드에서 X로 최단거리는 X를 출발지로 한 거꾸로 된 그래프 다익스트라
"""

N, M, X = map(int, input().split())
graph1 = {i: {} for i in range(1, N+1)}
graph2 = {i: {} for i in range(1, N+1)}
for _ in range(M):
    A, B, T = map(int, input().split())
    graph1[A][B] = T
    graph2[B][A] = T

def dijkstar(graph, start):
    unvisited = set(graph.keys())
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

    return distances

from_X = dijkstar(graph1, X)
to_X = dijkstar(graph2, X)
r = 0
for i in range(1, N+1):
    r = max(r, from_X[i]+to_X[i])
print(r)