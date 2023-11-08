"""
A → B
"""
from collections import deque

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    while q:
        n, count = q.popleft()
        n1, n2 = n*2, int(str(n)+'1')
        if n1 < b:
            q.append((n1, count+1))
        elif n1 == b:
            return count+1
        if n2 < b:
            q.append((n2, count+1))
        elif n2 == b:
            return count+1
    return -2

A, B = map(int, input().split())
print(bfs(A, B)+1)