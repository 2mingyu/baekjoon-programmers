"""
서강그라운드

import sys


n, m, r = map(int, input().split())
t = [0] + [int(x) for x in sys.stdin.readline().split()]
graph = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l
for i in range(n+1):
    graph[i][i] = 0

for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

ans = 0
for dropZone in range(1, n+1):
    obtainedItems = 0
    for searchArea in range(1, n+1):
        if graph[dropZone][searchArea] <= m:
            obtainedItems += t[searchArea]
    ans = max(ans, obtainedItems)

print(ans)
이거 왜틀리는데 밑에랑 똑같잖아 변수이름만 다르잖아 왜틀리는데
"""


import sys

INF = sys.maxsize
n, m, r = map(int, input().split())
t = [0] + [int(x) for x in sys.stdin.readline().split()]
graph = [[INF] * (n+1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l
for i in range(n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            tmp += t[j]
    ans = max(ans, tmp)

print(ans)