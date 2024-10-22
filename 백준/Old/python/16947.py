"""
서울 지하철 2호선

간선의 개수와 정점의 개수가 같은 양방향 연결 그래프는 사이클을 정확히 하나 갖는다. -> 순환선은 무조건 한 개

from collections import deque
import sys
sys.setrecursionlimit(10**8)

N = int(input())
A = [set() for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    A[a].add(b)
    A[b].add(a)

def check_rotate(start, current, c):
    global flag
    if start == current and c >= 2:
        flag = True
        return
    visited[current] = True
    for next in A[current]:
        if not visited[next]:
            check_rotate(start, next, c+1)
        elif next == start and c >= 2:
            check_rotate(start, next, c)

isRotate = [False] * (N+1)
for i in range(1, N+1):
    visited = [False] * (N+1)
    flag = False
    check_rotate(i, i, 0)
    if flag: isRotate[i] = True

def find_rotate():
    q = deque()
    for i in range(1, N+1):
        if isRotate[i]:
            r[i] = 0
            q.append(i)
    while q:
        current = q.popleft()
        for next in A[current]:
            if r[next] == -1:
                q.append(next)
                r[next] = r[current] + 1


r = [-1] * (N+1)
find_rotate()

print(*r[1:])

==========
시간초과 계속 떠서 다른 방법 찾기.
지선의 끝은 간선이 한 개
end는 지선의 끝인 정점들의 리스트
N = int(input())
graph = {i: [] for i in range(1, N+1)}
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

end = []
for node in graph:
    if len(graph[node]) == 1:
        end.append(node)

r = [0] * (N+1)
for e in end:
    q = [e, graph[e][0]]
    while True:
        current = q[-1]
        before = q[-2]
        graph[current].remove(before)
        if len(graph[current]) > 1:
            break
        q.append(graph[current][0])
    c = 0
    while q:
        r[q.pop()] = c
        c += 1

print(*r[1:])

이것도 안됨. 트리 Y 모양 생각.
"""
from collections import deque
import sys
sys.setrecursionlimit(10**8)

N = int(input())
A = [set() for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    A[a].add(b)
    A[b].add(a)

def check_rotate(route, c):
    global flag
    if flag:
        return
    for i in A[route[-1]]:
        if i == route[0] and c >= 2:
            for j in route:
                isRotate[j] = True
            flag = 1
            return
        if not visited[i]:
            visited[i] = 1
            check_rotate(route + [i], c+1)
            visited[i] = 0

isRotate = [False] * (N+1)
visited = [False] * (N+1)
flag = 0
for i in range(1, N+1):
    visited[i] = 1
    check_rotate([i], 0)
    visited[i] = 0


r = [-1] * (N+1)
s = 0
for i in range(1, N+1):
    if isRotate[i]:
        s = i
        break
q = deque()
visited = [False] * (N+1)
q.append((s, 0))
visited[s] = True
r[s] = 0
while q:
    current, distance = q.popleft()
    for next in A[current]:
        if not visited[next]:
            visited[next] = True
            if isRotate[next]:
                r[next] = 0
                q.append((next, 0))
            else:
                r[next] = distance + 1
                q.append((next, distance+1))

print(*r[1:])