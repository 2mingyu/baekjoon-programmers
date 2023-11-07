"""
최소비용 구하기 2

이미 버스 있는데도 값 더 큰 버스가 들어올 수도 있다고 ..
if b in bus[a]: bus[a][b] = min(bus[a][b], c)
else: bus[a][b] = c
"""
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = {i:{} for i in range(n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    if b in bus[a]: bus[a][b] = min(bus[a][b], c)
    else: bus[a][b] = c
start, end = map(int, input().split())

distances = [float('INF')] * (n+1)
route = ['' for _ in range(n+1)]
route_len = [0] * (n+1)
q = []
distances[start] = 0
route[start] = str(start)
route_len[start] = 1
heapq.heappush(q, (0, start))
while q:
    current_distance, current_node = heapq.heappop(q)
    if current_distance > distances[current_node]: continue
    for neighbor in bus[current_node]:
        distance = current_distance + bus[current_node][neighbor]
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            route[neighbor] = route[current_node] + ' ' + str(neighbor)
            route_len[neighbor] = route_len[current_node] + 1
            heapq.heappush(q, (distance, neighbor))

print(distances[end])
print(route_len[end])
print(route[end])