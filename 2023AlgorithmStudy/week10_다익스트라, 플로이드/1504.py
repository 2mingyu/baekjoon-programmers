"""
특정한 최단 경로
"""
import sys
import heapq

def dijkstra(start):
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())

distances = [sys.maxsize] * (N+1)
dijkstra(1)
one_v1 = distances[v1]
one_v2 = distances[v2]

distances = [sys.maxsize] * (N+1)
dijkstra(v1)
v1_N = distances[N]
v1_v2 = distances[v2]

distances = [sys.maxsize] * (N+1)
dijkstra(v2)
v2_N = distances[N]
v2_v1 = distances[v1]

if v1_v2 == sys.maxsize:
    print(-1)
elif one_v1 == sys.maxsize and one_v2 == sys.maxsize:
    print(-1)
elif v1_N == sys.maxsize and v2_N == sys.maxsize:
    print(-1)
elif one_v1 == sys.maxsize or v2_N == sys.maxsize:
    print(one_v2 + v2_v1 + v1_N)
elif one_v2 == sys.maxsize or v1_N == sys.maxsize:
    print(one_v1 + v1_v2 + v2_N)
else:
    print(min(one_v1 + v1_v2 + v2_N, one_v2 + v2_v1 + v1_N))