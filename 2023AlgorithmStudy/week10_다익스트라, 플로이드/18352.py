"""
특정 거리의 도시 찾기
"""
import heapq
import sys
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

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append([B, 1]) # 가중치(거리/길이)는 전부 1

distances = [sys.maxsize] * (N+1)
dijkstra(X)

results = []
for i in range(len(distances)):
    if  distances[i] == K:
        results.append(i)

if results:
    for r in results: print(r)
else:
    print(-1)