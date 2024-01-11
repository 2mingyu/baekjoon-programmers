"""
0과 1

모듈러 연산 !
"""
from collections import deque

def f(n):
    q = deque([('1', 1)])
    visited = [False] * 20001
    visited[1] = True
    while q:
        x, m = q.popleft()
        if m == 0:
            return x
        if len(x) > 100:
            return 'BRAK'
        a = (m * 10) % n
        b = (m*10 + 1) % n
        if not visited[a]:
            q.append((x+'0', a))
            visited[a] = True
        if not visited[b]:
            q.append((x+'1', b))
            visited[b] = True
    return 'BRAK'

T = int(input())
for _ in range(T):
    N = int(input())
    print(f(N))