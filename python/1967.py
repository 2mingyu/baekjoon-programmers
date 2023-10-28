"""
트리의 지름

visited[start] = 1
을 빼먹지 말자
"""
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0] * (n+1)
    longest_node, longest_length = start, 0
    visited[start] = 1
    q = deque([(start, 0)])
    while q:
        node, length = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                q.append((neighbor, length+graph[node][neighbor]))
                if length + graph[node][neighbor] > longest_length:
                    longest_node = neighbor
                    longest_length = length + graph[node][neighbor]
    return longest_node, longest_length

n = int(input())
graph = {i: {} for i in range(1, n+1)}
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

ln, ll = bfs(1)
ln, ll = bfs(ln)
print(ll)
