"""
BFS 스페셜 저지

아 양방향 그래프였어 .
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
E = {i+1:set() for i in range(N)}
for _ in range(N-1):
    a, b = map(int, input().split())
    E[a].add(b)
    E[b].add(a)
s = list(map(int, input().split()))
if s[0] != 1:
    print(0)
    exit()

q = deque([1])
i = 1
while q:
    x = q.popleft()
    j = 0
    l = len(E[x])
    while j < l:
        y = s[i]
        if y in E[x]:
            E[x].remove(y)
            E[y].remove(x)
            q.append(y)
            j += 1
            i += 1
        else:
            print(0)
            exit()
print(1)