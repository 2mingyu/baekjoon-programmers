from collections import deque
N = int(input())
d = deque([N])
for i in range(N-1, 0, -1):
    d.appendleft(i)
    for j in range(i):
        d.appendleft(d.pop())
print(*d)