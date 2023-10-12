"""
헌내기는 친구가 필요해

간단한 BFS
"""
from collections import deque
N, M = map(int, input().split())
visited = []
m = []
y, x = 0, 0
for i in range(N):
    a = input()
    visited.append([False] * M)
    m.append(a)
    if 'I' in a: y, x = i, a.index('I')
count = 0
visited[y][x] = True
q = deque([(y,x)])
while q:
    y, x = q.popleft()
    for d in [1,0], [0,1], [-1,0], [0, -1]:
        ny, nx = y+d[0], x+d[1]
        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if m[ny][nx] == 'O':
                    q.append((ny,nx))
                elif m[ny][nx] == 'P':
                    q.append((ny,nx))
                    count += 1
if count: print(count)
else: print('TT')