import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
m = [list(input()) for _ in range(N)]
q = deque([(0, 0)])
while q:
    y, x = q.popleft()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M and m[ny][nx] == '0':
            m[ny][nx] = '2'
            q.append((ny, nx))
s = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (m[i-1][j-1] != '2')
Q = int(input())
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    t = s[r2][c2] - s[r1-1][c2] - s[r2][c1-1] + s[r1-1][c1-1]
    print(f'No {t}' if t else 'Yes')