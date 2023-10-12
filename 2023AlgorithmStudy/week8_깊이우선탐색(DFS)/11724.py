"""
연결 요소의 개수
방향 없는 그래프, 같은 간선은 한 번만 주어진다.

import sys
sys.setrecursionlimit(1000000)

def check(a, CCC):
    vertex[a] = CCC
    for b in range(1, N+1):
        if vertex[b] == 0:
            if edge[a][b] == 1 or edge[b][a] == 1:
                check(b, CCC)

N, M = map(int, input().split())
vertex = [0 for _ in range(N+1)]
edge = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u][v] = 1
CC = 0
for v in range(1, N+1):
    if vertex[v] == 0:
        for n in range(1, N+1):
            if edge[v][n] == 1 or edge[n][v] == 1:
                CC += 1
                vertex[v] = CC
                check(n, CC)
                break
print(CC)

edge에 간선을 1로 저장하는 방식. 시간초과 뜬다
아래는 각각의 vertex가 자신이 연결된 곳만 저장하는 방식

간선 없이 혼자 있는 정점도 구성요소가 될 수 있다는 걸 생각 못해서 많이 틀렸다 ..
"""
import sys
sys.setrecursionlimit(10000000)

def check(a):
    vertex[a] = True
    for b in edge[a]:
        if not vertex[b]:
            check(b)

N, M = map(int, input().split())
edge = [[] for _ in range(N+1)]
vertex = [False] * (N+1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)
CC = 0
for v in range(1, N+1):
    if not vertex[v]:
        CC += 1
        check(v)
print(CC)

