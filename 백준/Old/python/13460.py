"""
구슬 탈출 2

if blue: continue 를 exit()로 해서 고생했네..
"""
from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

Ry = Rx = By = Bx = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            Ry, Rx = i, j
        elif board[i][j] == 'B':
            By, Bx = i, j

q = deque([(Ry, Rx, By, Bx, 0)])
visited = {(Ry, Rx, By, Bx)}
while q:
    Ry, Rx, By, Bx, count = q.popleft()
    if count == 10:
        print(-1)
        exit()

    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        Rny, Rnx, Bny, Bnx = Ry, Rx, By, Bx
        red = blue = False
        while board[Rny+dy][Rnx+dx] != '#':     # 벽을 만날 때까지 이동
            if board[Rny+dy][Rnx+dx] == 'O':    # 다음 위치가 구멍이면
                red = True
                break                           # 그만 이동
            Rny += dy; Rnx += dx
        while board[Bny+dy][Bnx+dx] != '#':
            if board[Bny+dy][Bnx+dx] == 'O':
                blue = True
                break
            Bny += dy; Bnx += dx
        if blue:
            continue
        if red:
            print(count+1)
            exit()

        if Rny == Bny and Rnx == Bnx:   # 빨강 파랑 위치 겹쳤을 때
            if (dy, dx) == (0, -1):    # 왼쪽으로 기울이기 였다면
                if Rx < Bx:             # 이전 위치가 빨강이 더 왼쪽이었다면
                    Bnx += 1             # 현재 파랑 위치를 한 칸 오른쪽으로
                else:
                    Rnx += 1
            elif (dy, dx) == (0, 1):
                if Rx < Bx:
                    Rnx -= 1
                else:
                    Bnx -= 1
            elif (dy, dx) == (-1, 0):
                if Ry < By:
                    Bny += 1
                else:
                    Rny += 1
            elif (dy, dx) == (1, 0):
                if Ry < By:
                    Rny -= 1
                else:
                    Bny -= 1

        if (Rny, Rnx, Bny, Bnx) not in visited:
            q.append((Rny, Rnx, Bny, Bnx, count+1))
            visited.add((Rny, Rnx, Bny, Bnx))

print(-1)