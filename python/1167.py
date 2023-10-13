"""
트리의 지름
https://johoonday.tistory.com/217
시작 지점 (1) 부터 가장 먼 곳을 구하고, 그 곳부터 가장 먼 곳을 다시 한번 구해야 함
"""
from collections import deque
V = int(input())
tree = {i+1: {} for i in range(V)}
for _ in range(V):
    l = list(map(int, input().split()))
    n = 1
    while l[n] != -1:
        tree[l[0]][l[n]] = l[n+1]
        n += 2

visited = {1}
q = deque([(1, 0)])
maxNode, maxValue = 1, 0
while q:
    node, value = q.popleft()
    if value > maxValue:
        maxNode, maxValue = node, value
    for neighbor in tree[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append((neighbor, value + tree[node][neighbor]))

visited = {maxNode}
q = deque([(maxNode, 0)])
maxNode, maxValue = maxNode, 0
while q:
    node, value = q.popleft()
    if value > maxValue:
        maxNode, maxValue = node, value
    for neighbor in tree[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append((neighbor, value + tree[node][neighbor]))

print(maxValue)