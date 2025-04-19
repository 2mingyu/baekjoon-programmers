from collections import deque

SIZE = 500
INF = float('inf')

board = [[0]*(SIZE+1) for _ in range(SIZE+1)]
dist = [[INF]*(SIZE+1) for _ in range(SIZE+1)]
N = int(input())
for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 > X2: X1, X2 = X2, X1
    if Y1 > Y2: Y1, Y2 = Y2, Y1
    for y in range(Y1, Y2+1):
        for x in range(X1, X2+1):
            board[y][x] = 1
M = int(input())
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 > X2: X1, X2 = X2, X1
    if Y1 > Y2: Y1, Y2 = Y2, Y1
    for y in range(Y1, Y2+1):
        for x in range(X1, X2+1):
            board[y][x] = INF
board[0][0] = INF

q = deque()
q.append((0, 0))
dist[0][0] = 0
while q:
    y, x = q.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y+dy, x+dx
        if 0 <= ny <= 500 and 0 <= nx <= 500:
            w = board[ny][nx]
            if dist[ny][nx] > dist[y][x] + w:
                dist[ny][nx] = dist[y][x] + w
                if w: q.append((ny, nx))
                else: q.appendleft((ny, nx))

ans = dist[SIZE][SIZE]
print(ans if ans != INF else -1)