"""
케빈 베이컨의 6단계 법칙
"""
import sys

N, M = map(int, input().split())
graph = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for m in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

kbNum = [0 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        kbNum[i] += graph[i][j]
result = 0
kbMin = sys.maxsize
for i in range(1, N+1):
    if kbNum[i] < kbMin:
        result = i
        kbMin = kbNum[i]
print(result)