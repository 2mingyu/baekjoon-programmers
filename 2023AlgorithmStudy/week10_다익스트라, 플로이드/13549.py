"""
숨바꼭질 3
heapq.heappop(heap)은 heap에서 가장 작은 값을 제거하고 반환
item이 리스트인 경우엔 첫 번째 값을 기준으로 비교
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

        for neighbor, weight in [[current_vertex-1, 1], [current_vertex+1, 1], [current_vertex*2, 0]]:
            if 0 <= neighbor <= 100000:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

N, K = map(int, input().split())
distances = [sys.maxsize] * 100001
dijkstra(N)
print(distances[K])