"""
최소비용 구하기
우선순위 큐를 이용한 다익스트라
최댓값을 100000 말고 sys.maxsize 써야하네?
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


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distances = [sys.maxsize for _ in range(N+1)]
for _ in range(M):
    depart, arrive, cost = map(int, sys.stdin.readline().split())
    graph[depart].append((arrive, cost))
depart, arrive = map(int, input().split())
dijkstra(depart)
print(distances[arrive])