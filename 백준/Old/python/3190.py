"""
뱀

오른쪽 0 아래 1 왼쪽 2 위 3
board에서 사과 1, 뱀 몸 2
snake 큐에서 왼쪽이 머리, 오른쪽이 꼬리
"""
from collections import deque
N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1
rot = {}
L = int(input())
for _ in range(L):
    X, C = input().split()
    rot[int(X)] = C

direction = 0
t = 0
snake = deque()
snake.append((0,0))
board[0][0] = 2
while True:
    if t in rot:
        if rot[t] == 'D': direction = (direction + 1) % 4
        else: direction = (direction - 1) % 4
    y, x = snake.popleft()
    if direction == 0: ny, nx = y, x+1
    elif direction == 1: ny, nx = y+1, x
    elif direction == 2: ny, nx = y, x-1
    else: ny, nx = y-1, x
    if 0 <= ny < N and 0 <= nx < N:
        if board[ny][nx] == 2:
            break
        elif board[ny][nx] == 1:
            board[ny][nx] = 2
            snake.appendleft((y, x))
            snake.appendleft((ny, nx))
        else:
            board[ny][nx] = 2
            snake.appendleft((y, x))
            snake.appendleft((ny, nx))
            ty, tx = snake.pop()
            board[ty][tx] = 0
        t += 1
    else:
        break
print(t+1)