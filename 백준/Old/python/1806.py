"""
부분합
"""
from collections import deque
N, S = map(int, input().split())
A = deque(list(map(int, input().split())))
B = deque()
s = 0
while A and s < S:
    B.append(A.popleft())
    s += B[-1]
if s < S:
    print(0)
    exit()
r = len(B)
while A:
    if s - B[0] >= S:
        s -= B[0]
        B.popleft()
        r = min(r, len(B))
    else:
        B.append(A.popleft())
        s += B[-1]
while B:
    s -= B[0]
    B.popleft()
    if s >= S:
        r = min(r, len(B))
    else:
        break
print(r)