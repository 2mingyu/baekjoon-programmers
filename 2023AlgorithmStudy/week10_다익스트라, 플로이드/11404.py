"""
플로이드

참고 - 11403
"""
import sys

n = int(input())
m = int(input())
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])

for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == sys.maxsize: print(0, end=" ")
        elif i == j: print(0, end=" ")
        else: print(graph[i][j], end=" ")
    print()