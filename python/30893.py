"""
트리 게임

INU 코드페스티벌 2023 E번
"""
import sys
input = sys.stdin.readline
from collections import deque

N, S, E = map(int, input().split())
tree = {node: set() for node in range(1, N+1)}
visited = [False] * (N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].add(v)
    tree[v].add(u)

route = ''
q = deque()
q.append((S, str(S)))
visited[S] = True
while q:
    a, b = q.popleft()
    if a == E:
        route = b
        break
    for neighbor in tree[a]:
        if not visited[neighbor]:
            q.append((neighbor, b+' ' + str(neighbor)))
            visited[neighbor] = True
route = deque(route.split())
turn = 'First'
before = r = 0
while route:
    before = r
    r = int(route.popleft())
    if r == E: break
    if turn == 'First':
        turn = 'Second'
    elif turn == 'Second':
        tree[r].remove(before)
        if len(tree[r]) > 1:
            print('Second')
            exit(0)
        turn = 'First'
print('First')