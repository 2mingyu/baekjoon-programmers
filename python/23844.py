"""
트리 정리하기

INU 코드페스티벌 2021 D

최대한 자식이 적은 노드를 제거해야겠지
아래부터 제거해야되나
걍 dfs 탐색?
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(n, l):
    if level[l] < K:
        level[l] += 1
    for c in d[n]:
        if not visited[c]:
            visited[c] = True
            dfs(c, l+1)

N, K = map(int, input().split())
d = {node: set() for node in range(1, N+1)}
for i in range(N-1):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)

visited = [False] * (N+1)
level = [0] * (N+1)

visited[1] = True
dfs(1, 0)

print(sum(level))