from collections import deque
N = int(input())
T = int(input())
a = deque(list(map(int, input().split())))
b = list(map(int, input().split()))
for i in range(T):
    for j in range(b[i]-1):
        a.append(a.popleft())
    print(a[0], end=' ')