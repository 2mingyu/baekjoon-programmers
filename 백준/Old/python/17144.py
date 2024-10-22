"""
미세먼지 안녕!

시간 초과 나서 다시 짤 뻔 했는데 sys.stdin.readline 쓰고 pypy3로 돌리니 통과
"""
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
house = []
next_house = [[0]*C for _ in range(R)]
for _ in range(R):
    house.append(list(map(int, input().split())))
air1 = 0
air2 = 0
for y in range(R):
    if house[y][0] == -1:
        air1 = y
        air2 = y+1
        break

for _ in range(T):
    for y in range(R):
        for x in range(C):
            next_house[y][x] += house[y][x]
            if y == air1 and x == 0:
                continue
            elif y == air2 and x == 0:
                continue
            if y-1 >= 0:
                if house[y-1][x] != -1:
                    next_house[y][x] -= house[y][x] // 5
                    next_house[y][x] += house[y-1][x] // 5
            if x-1 >= 0:
                if house[y][x-1] != -1:
                    next_house[y][x] -= house[y][x] // 5
                    next_house[y][x] += house[y][x-1] // 5
            if y+1 < R:
                if house[y+1][x] != -1:
                    next_house[y][x] -= house[y][x] // 5
                    next_house[y][x] += house[y+1][x] // 5
            if x+1 < C:
                if house[y][x+1] != -1:
                    next_house[y][x] -= house[y][x] // 5
                    next_house[y][x] += house[y][x+1] // 5

    for y in range(air1, 0, -1):
        next_house[y][0] = next_house[y-1][0]
    for x in range(0, C-1, 1):
        next_house[0][x] = next_house[0][x+1]
    for y in range(0, air1, 1):
        next_house[y][C-1] = next_house[y+1][C-1]
    for x in range(C-1, 1, -1):
        next_house[air1][x] = next_house[air1][x-1]
    next_house[air1][1] = 0

    for y in range(air2, R-1, 1):
        next_house[y][0] = next_house[y+1][0]
    for x in range(0, C-1, 1):
        next_house[R-1][x] = next_house[R-1][x+1]
    for y in range(R-1, air2, -1):
        next_house[y][C-1] = next_house[y-1][C-1]
    for x in range(C-1, 1, -1):
        next_house[air2][x] = next_house[air2][x-1]
    next_house[air2][1] = 0

    next_house[air1][0] = -1
    next_house[air2][0] = -1

    house = next_house[:]
    next_house = [[0]*C for _ in range(R)]

result = 0
for y in range(R):
    for x in range(C):
        result += house[y][x]
print(result+2)