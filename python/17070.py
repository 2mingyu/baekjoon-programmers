"""
파이프 옮기기 1
dp로 y, x, shape
shape로는 가로, 세로, 대각선
+ bps?

시간초과 코드
from collections import deque
N = int(input())
house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

result = 0
q = deque()
q.append((0, 1, 0))
while q:
    y, x, shape = q.popleft()
    if y == x == N-1:
        result += 1
        continue
    if shape == 0:
        if x+1 < N and house[y][x+1] == 0:
            q.append((y, x+1, 0))
        if x+1 < N and y+1 < N and house[y][x+1] == house[y+1][x+1] == house[y+1][x] == 0:
            q.append((y+1, x+1, 2))
    elif shape == 1:
        if y+1 < N and house[y+1][x] == 0:
            q.append((y+1, x, 1))
        if x+1 < N and y+1 < N and house[y][x+1] == house[y+1][x+1] == house[y+1][x] == 0:
            q.append((y+1, x+1, 2))
    elif shape == 2:
        if x+1 < N and house[y][x+1] == 0:
            q.append((y, x+1, 0))
        if y+1 < N and house[y+1][x] == 0:
            q.append((y+1, x, 1))
        if x+1 < N and y+1 < N and house[y][x+1] == house[y+1][x+1] == house[y+1][x] == 0:
            q.append((y+1, x+1, 2))

print(result)

17069 파이프 옮기기 2와 같다
저건 잘 풀어놓고 이건 못풀었네
"""
N = int(input())
house = [[1] * (N+2)]
m = [[[0 for k in range(3)] for j in range(N+2)] for i in range(N+2)]
for _ in range(N):
    tmp = [1] + list(map(int, input().split())) + [1]
    house.append(tmp)
house.append([1] * (N+2))
m[1][2][0] = 1
for row in range(1, N+1):
    for col in range(2, N+1):
        if house[row][col+1] != 1:
            m[row][col+1][0] += m[row][col][0]  # 가로->가로
            m[row][col+1][0] += m[row][col][1]  # 대각->가로
        if house[row][col+1] != 1 and house[row+1][col+1] !=1  and house[row+1][col] != 1:
            m[row+1][col+1][1] += m[row][col][0]    # 가로->대각
            m[row+1][col+1][1] += m[row][col][1]    # 대각->대각
            m[row+1][col+1][1] += m[row][col][2]    # 세로->대각
        if house[row+1][col] != 1:
            m[row+1][col][2] += m[row][col][1]    # 대각->세로
            m[row+1][col][2] += m[row][col][2]    # 세로->세로
print(sum(m[N][N]))