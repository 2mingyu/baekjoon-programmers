"""
유령의 집 탈출하기

INU 코드페스티벌 2023 F번

t초의 유령의 상태는 (t+초기상태) % 4
"""
"""
대회 때 제출하고 실패한 코드
import sys
input = sys.stdin.readline
from collections import deque

def ghostok(nx, ny, t):
    # 위쪽 확인
    for i in range(nx-1, -1, -1):
        if house[i][ny] == '#':
            break
        elif house[i][ny] in ['0', '1', '2', '3']:
            ghoststatus = (int(house[i][ny]) + (t)) % 4
            if ghoststatus == 1: return False
            else: break
    # 아래쪽 확인
    for i in range(nx+1, N, 1):
        if house[i][ny] == '#':
            break
        elif house[i][ny] in ['0', '1', '2', '3']:
            ghoststatus = (int(house[i][ny]) + (t)) % 4
            if ghoststatus == 3: return False
            else: break
    # 왼쪽 확인
    for i in range(ny-1, -1, -1):
        if house[nx][i] == '#':
            break
        elif house[nx][i] in ['0', '1', '2', '3']:
            ghoststatus = (int(house[nx][i]) + (t)) % 4
            if ghoststatus == 0: return False
            else: break
    # 오른쪽 확인
    for i in range(ny+1, M, 1):
        if house[nx][i] == '#':
            break
        elif house[nx][i] in ['0', '1', '2', '3']:
            ghoststatus = (int(house[nx][i]) + (t)) % 4
            if ghoststatus == 2: return False
            else: break
    return True

N, M = map(int, input().split())
Sx, Sy, Ex, Ey = map(int, input().split())
Sx -= 1
Sy -= 1
Ex -= 1
Ey -= 1
house = [[] for _ in range(N)]
visited = [[] for _ in range(N)]
for n in range(N):
    tmp = input().split()[0]
    for m in range(M):
        house[n].append(tmp[m])
        visited[n].append(False)

q = deque()
q.append((Sx, Sy, 0, 0))
visited[Sx][Sy] = True
while q:
    x, y, t, s = q.popleft()
    # print()
    # print(x, y, t, s, end=' => ')
    if x == Ex and y == Ey:
        print(t)
        exit(0)
    if s == 4:
        continue
    for dx, dy in ((1,0), (-1, 0), (0, 1), (0, -1), (0, 0)):
        nx, ny = x+dx, y+dy
        if dx == 0 and dy == 0:
            if ghostok(nx, ny, t+1):
                # print(nx, ny, t+1, s+1, end=' , ')
                q.append((nx, ny, t+1, s+1))
        else:
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if house[nx][ny] not in ['#', '0', '1', '2', '3']:
                    if ghostok(nx, ny, t+1):
                        q.append((nx, ny, t+1, 0))
                        # print(nx, ny, t+1, 0, end=' , ')
                        visited[nx][ny] = True
print('GG')
"""
from collections import deque

N, M = map(int, input().split())
Sx, Sy, Ex, Ey = map(int, input().split())
Sx -= 1; Sy -= 1; Ex -= 1; Ey -= 1
init = []
house = [[] for _ in range(4)]
visited = [[] for _ in range(4)]
for _ in range(N):
    temp = list(input())
    init.append(temp[:])
    for t in range(4):
        house[t].append(temp[:])
        visited[t].append([False]*M)

for i in range(N):
    for j in range(M):
        if init[i][j] in ['0', '1', '2', '3']:
            for t in range(4):
                g = ((int(init[i][j])) + t) % 4
                house[t][i][j] = '#'
                if g == 0:
                    for y in range(j+1, M, 1):
                        if init[i][y] in ['#', '0', '1', '2', '3']: break
                        house[t][i][y] = '#'
                elif g == 1:
                    for x in range(i+1, N, 1):
                        if init[x][j] in ['#', '0', '1', '2', '3']: break
                        house[t][x][j] = '#'
                elif g == 2:
                    for y in range(j-1, -1, -1):
                        if init[i][y] in ['#', '0', '1', '2', '3']: break
                        house[t][i][y] = '#'
                elif g == 3:
                    for x in range(i-1, -1, -1):
                        if init[x][j] in ['#', '0', '1', '2', '3']: break
                        house[t][x][j] = '#'

q = deque()
q.append((0, Sx, Sy))
visited[0][Sx][Sy] = True
while q:
    t, x, y = q.popleft()
    if x == Ex and y == Ey:
        print(t)
        exit(0)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
        nt, nx, ny = t+1, x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nt%4][nx][ny] and house[nt%4][nx][ny] != '#':
                q.append((nt, nx, ny))
                visited[nt%4][nx][ny] = True
print('GG')