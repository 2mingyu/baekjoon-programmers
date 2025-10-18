N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
K = {'W': {'event': input(), 'dy': -1, 'dx': 0},
     'A': {'event': input(), 'dy': 0, 'dx': -1},
     'S': {'event': input(), 'dy': 1, 'dx': 0},
     'D': {'event': input(), 'dy': 0, 'dx': 1}}
C = input()
y, x = 0, 0
for i in range(N):
    for j in range(N):
        if m[i][j] == 2:
            y, x = i, j
            break
p = ''
def move(c):
    global y, x
    dy, dx = K[c]['dy'], K[c]['dx']
    ny, nx = y+dy, x+dx
    if 0 <= ny < N and 0 <= nx < N and m[ny][nx] != 1: y, x = ny, nx

for c in C:
    for k in 'WASD':
        event = ''
        if k == c and k == p: event = 'Stay'
        elif k == c and k != p: event = 'Down'
        elif k != c and k == p: event = 'Up'
        if event == K[k]['event']: move(k)
    p = c
print(y+1, x+1)