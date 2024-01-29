"""
백조의 호수

q1, q2: 백조
q3: 물
처음에 틀렸던 것: q3이 없었어서, 백조가 없는 공간에서 녹는 것을 고려하지 못했음.
"""
from collections import deque

def bfs_q1():
    while q1:
        y, x, d = q1.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited_swan[ny][nx]:
                    if A[ny][nx] == 'X':
                        q1_next.append((ny, nx, d+1))
                        visited_swan[ny][nx] = 1
                    else:
                        q1.append((ny, nx, d))
                        visited_swan[ny][nx] = 1
                elif visited_swan[ny][nx] == 2:
                    print(d)
                    exit(0)

def bfs_q2():
    while q2:
        y, x, d = q2.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited_swan[ny][nx]:
                    if A[ny][nx] == 'X':
                        q2_next.append((ny, nx, d+1))
                        visited_swan[ny][nx] = 2
                    else:
                        q2.append((ny, nx, d))
                        visited_swan[ny][nx] = 2
                elif visited_swan[ny][nx] == 1:
                    print(d+1)
                    exit(0)

def bfs_q3():
    while q3:
        y, x = q3.popleft()
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                if not visited_water[ny][nx]:
                    if A[ny][nx] == 'X':
                        A[ny][nx] = '.'
                        q3_next.append((ny, nx))
                        visited_water[ny][nx] = 1
                    else:
                        q3.append((ny, nx))
                        visited_water[ny][nx] = 1

R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]
visited_swan = [[0] * C for _ in range(R)]
visited_water = [[False] * C for _ in range(R)]
q1 = deque()
q1_next = deque()
q2 = deque()
q2_next = deque()
q3 = deque()
q3_next = deque()
for i in range(R):
    for j in range(C):
        if A[i][j] == 'L':
            if q1:
                q2.append((i, j, 0))
                visited_swan[i][j] = 2
            else:
                q1.append((i, j, 0))
                visited_swan[i][j] = 1
        if A[i][j] == '.':
            q3.append((i, j))
            visited_water[i][j] = True

while True:
    bfs_q1()
    bfs_q2()
    bfs_q3()
    q1 = deque(q1_next)
    q2 = deque(q2_next)
    q3 = deque(q3_next)
    q1_next = deque()
    q2_next = deque()
    q3_next = deque()