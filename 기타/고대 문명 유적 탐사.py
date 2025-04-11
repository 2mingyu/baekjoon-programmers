# https://www.codetree.ai/ko/frequent-problems/problems/ancient-ruin-exploration/description?introductionSetId=&bookmarkId=
# SAMSUNG SW 역량 테스트 2024 상반기 오전 1번 문제

from collections import deque


def rotated(paramRelics, y, x, deg):
    r = [paramRelics[i][:] for i in range(5)]  # 깊은 복사
    repeat = 0
    if deg == 90: repeat = 1
    elif deg == 180: repeat = 2
    elif deg == 270: repeat = 3
    for _ in range(repeat):
        r[y-1][x-1], r[y+1][x-1], r[y+1][x+1], r[y-1][x+1] = r[y+1][x-1], r[y+1][x+1], r[y-1][x+1], r[y-1][x-1]
        r[y-1][x], r[y][x-1], r[y+1][x], r[y][x+1] = r[y][x-1], r[y+1][x], r[y][x+1], r[y-1][x]
    return r


def bfs(i, j, k, r, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    t = [(i, j)]
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx] and r[ny][nx] == k:
                t.append((ny, nx))
                visited[ny][nx] = True
                q.append((ny, nx))
    if len(t) >= 3:
        for e in t:
            y, x = e[0], e[1]
            r[y][x] = 0
        return len(t)
    else:
        return 0


def get_relics(r):
    v = 0
    visited = [[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if r[i][j]:
                x = bfs(i, j, r[i][j], r, visited)
                v += x
    return v


def fill_relics(r):
    for x in [0, 1, 2, 3, 4]:
        for y in [4, 3, 2, 1, 0]:
            if r[y][x] == 0:
                r[y][x] = wall.popleft()


K, M = map(int, input().split())
relics = [list(map(int, input().split())) for _ in range(5)]
wall = deque(map(int, input().split()))
for _ in range(K):
    # [1] 탐사 진행
    max_value, max_x, max_y, max_d = 0, 0, 0, 0  # 유물 1차 획득 가치 최대로
    for d in [90, 180, 270]:    # 각도
        for x in [1, 2, 3]:     # 열
            for y in [1, 2, 3]: # 행
                rotatedRelics = rotated(relics, y, x, d)
                tmp_value = get_relics(rotatedRelics)   # 유물 1차 획득
                if tmp_value > max_value:
                    max_value, max_x, max_y, max_d = tmp_value, x, y, d
    if max_value == 0: break    # 탐사 즉시 종료
    relics = rotated(relics, max_y, max_x, max_d)
    # [2] 유물 획득
    value = 0
    while True: # 유물 연쇄 획득
        tmp_value = get_relics(relics) # 유물 획득
        if tmp_value:
            value += tmp_value
            fill_relics(relics)    # 조각 채우기
        else:
            break
    print(value, end=' ')