"""
숨바꼭질 5

미리 도착해서 와리가리 하는 경우, 홀짝 시간 구분.. 어렵구만
"""
from collections import deque

N, K = map(int, input().split())
if N == K: print(0); exit()
t = 1; K += t
q1 = deque([deque([N])])
visited = [[0]*500001 for _ in range(2)]
while q1 and K <= 500000:
    q2 = q1.popleft()
    q3 = deque()
    while q2:
        X = q2.popleft()
        for dx in -1, 1, X:
            nX = X+dx
            if 0 <= nX <= 500000 and not visited[t%2][nX]:
                q3.append(nX)
                visited[t%2][nX] = t
    if q3: q1.append(q3)
    if visited[t%2][K]: print(t); exit()
    t += 1; K += t

print(-1)
