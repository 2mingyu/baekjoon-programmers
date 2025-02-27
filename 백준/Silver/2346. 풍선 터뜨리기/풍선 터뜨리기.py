from collections import deque

N = int(input())
q = deque(enumerate(map(int, input().split())))
while q:
    print(q[0][0]+1, end=' ')
    x = q.popleft()[1]
    while (x < 0 or 1 < x) and q:
        if x > 0:
            q.append(q.popleft())
            x -= 1
        else:
            q.appendleft(q.pop())
            x += 1