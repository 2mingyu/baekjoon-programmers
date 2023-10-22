"""
최단경로

입력 문제로 계속 틀렸다 .
1 2 1 들어오고 나중에 1 2 10 들어올 수도 있음 ..
"""
import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
INF = float('infinity')
graph = {}
distances = [INF]
for i in range(1, V+1):
    graph[i] = {}
    distances.append(INF)
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        if w < graph[u][v]:
            graph[u][v] = w
    else:
        graph[u][v] = w

distances[K] = 0
q = [(distances[K],K)]
while q:
    current_distance, current_node = heapq.heappop(q)
    if current_distance <= distances[current_node]:
        for neighbor in graph[current_node]:
            new_distance = current_distance + graph[current_node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(q, (distances[neighbor], neighbor))

for i in range(1, V+1):
    if distances[i] == INF:
        print('INF')
    else:
        print(distances[i])