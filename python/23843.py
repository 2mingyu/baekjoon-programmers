"""
성냥개비

INU 코드페스티벌 2021 C
"""
from collections import deque
N, M = map(int, input().split())
t = deque(sorted(list(map(int, input().split())), reverse=True))
r = 0
con = [0] * M
while t:
    a = min(con)
    r += a
    for m in range(M):
        con[m] -= a
        if con[m] == 0 and t:
            con[m] = t.popleft()
r += max(con)
print(r)