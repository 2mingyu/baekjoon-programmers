"""
이분 그래프
"""
import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    q = deque([s])
    visited[s] = True
    group[s] = 1
    while q:
        x = q.popleft()
        for y in e[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = True
                group[y] = not group[x]
            else:
                if group[y] == group[x]:
                    return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    e = {i:set() for i in range(1, V+1)}
    visited = [False] * (V+1)
    group = [0] * (V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        e[u].add(v)
        e[v].add(u)
    flag = True
    for i in range(1, V+1):
        if not visited[i]:
             flag = bfs(i)
             if not flag:
                 break
    if flag: print("YES")
    else: print("NO")