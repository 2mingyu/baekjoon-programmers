"""
ACM Craft

t[7] = D[7] + max([t[i] for i in condition[7]])
BFS 같기도

graph[X] : X 지은 다음 지을 수 있는 건물들

위상 정렬 ..

stdin.readline 안써서 계속 시간 초과 났네..
"""
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    graph = {i: [] for i in range(N+1)}
    degree = [0] * (N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        degree[Y] += 1
    W = int(input())

    visited = [False] * (N+1)
    time = [0] * (N+1)
    q = deque()
    for node in graph:
        if degree[node] == 0:
            visited[node] = True
            time[node] = D[node]
            q.append(node)

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                time[neighbor] = max(time[node]+D[neighbor], time[neighbor])
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    if neighbor == W:
                        q = 0
                        break
                    visited[neighbor] = True
                    q.append(neighbor)
    print(time[W])