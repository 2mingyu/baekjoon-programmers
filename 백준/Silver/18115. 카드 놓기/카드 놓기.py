from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = [x for x in range(N, 0, -1)]
C = deque()
while A:
    x = A.pop()
    y = B.pop()
    if x == 1:
        C.appendleft(y)
    elif x == 2:
        t = C.popleft()
        C.appendleft(y)
        C.appendleft(t)
    elif x == 3:
        C.append(y)
print(*C)