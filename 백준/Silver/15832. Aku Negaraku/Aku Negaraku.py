from collections import deque
while True:
    N, M = map(int, input().split())
    if N+M == 0: exit()
    a = deque([x for x in range(1, N+1)])
    while len(a) > 1:
        for _ in range(M-1):
            a.append(a.popleft())
        a.popleft()
    print(a[0])