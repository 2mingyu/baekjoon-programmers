from collections import deque
n, T = map(int, input().split())
q = deque(map(int, input().split()))
s = 0
i = 0
while q:
    x = q.popleft()
    if s+x <= T:
        s += x
        i += 1
    else:
        break
print(i)