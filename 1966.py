"""
프린터 큐
"""
from collections import deque
for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    count = 1
    while q:
        m = max(q)
        now = q.popleft()
        if now == m:
            if M == 0:
                print(count)
                break
            count += 1
        else:
            q.append(now)
        if M == 0:
            M = len(q)-1
        else:
            M -= 1